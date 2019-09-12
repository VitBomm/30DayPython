from odoo import fields, api, models
from odoo.addons.xb_hr_time_mngt.models.common import get_crossover_in_period
from odoo.addons.xb_base.tools.date_utils import timezone_conversion
from odoo.addons.resource.models.resource import float_to_time
import xlrd
import pytz
import base64
import threading
from datetime import date, datetime
from calendar import monthrange
from odoo.exceptions import ValidationError, UserError
import logging

_logger = logging.getLogger(__name__)


class HrImport(models.TransientModel):
    _name = 'hr.import'

    def _default_date_from(self):
        now = date.today()
        start_date = date(now.year, now.month, 1)
        return start_date

    def _default_date_to(self):
        now = date.today()
        end_date = date(now.year, now.month,
                        monthrange(now.year, now.month)[1])
        return end_date

    file = fields.Binary(string="Timesheet Excel File",
                         help="Choice file to import timesheet")
    filename = filename = fields.Char("Filename")
    start_date = fields.Date(string="Timesheet Period",
                             help="The start date of timesheet", default=_default_date_from)
    end_date = fields.Date(string="Timesheet Period",
                           help="The end date of timesheet", default=_default_date_to)
    company_id = fields.Many2one('res.company', string="Company", help="Only import timesheet of one company at one time, \
        if you want more please press 'Ctrl' + 'W' or press shutdown button on your device, take a rest, sleep hard dream deep \
        In your dream maybe this feature maybe appear", default=lambda self: self.env.user.company_id)
    employee_ids = fields.Many2many('hr.employee', string="Employees")
    @api.onchange('end_date')
    def change_enddate(self):
        if self.start_date > self.end_date:
            raise UserError("End date must be greater than start date")

    def number_days_in_month_selected(self):
        if self.end_date.month != self.start_date.month:
            raise UserError(
                "Please Check Timesheet Period. Period days must be in same month!")
        return (self.end_date - self.start_date).days

    # Ham nay da chay
    @api.multi
    def action_import_timesheet(self):
        self.ensure_one()
        # check extension
        ext = self.filename.split('.')
        ext = ext[len(ext) - 1]
        # Get Start_Row, Start_Col, End_Col

        if not self.file or ext not in ['xls', 'xlsx']:
            raise UserError(
                'Please input correct format, file must be at xls or xlsx format!')
        number_days_in_month_selected = self.number_days_in_month_selected()
        COL_START = 7
        ROW_START = 8
        COL_END = COL_START + number_days_in_month_selected
        MSNV = 2

        # Read data from file
        data = base64.decodestring(self.file)
        excel = xlrd.open_workbook(file_contents=data)
        sheet = excel.sheet_by_index(0)
        vals = []

        # read 3 line at once
        # first attendance
        # second legal leaves
        # third leave unpaid
        for index in range(ROW_START, sheet.nrows, 3):
            if index < ROW_START:
                continue
            row_attendance = sheet.row(index)
            row_legal_leaves = sheet.row(index + 1)
            row_unpaid_leaves = sheet.row(index + 2)
            row_ot = sheet.row(index + 3)
            msnv = row_attendance[MSNV].value
            if not msnv:
                break

            ra = list(
                map(lambda x: x.value, row_attendance[COL_START: COL_END + 1]))
            rl = list(
                map(lambda x: x.value, row_legal_leaves[COL_START: COL_END + 1]))
            ru = list(
                map(lambda x: x.value, row_unpaid_leaves[COL_START: COL_END + 1]))
            ot = list(map(lambda x: x.value, row_ot[COL_START:COL_END + 1]))
            tmp = []

            for index in range(len(ra)):
                tmp += [[str(ra[index]).strip(), str(rl[index]).strip(),
                         str(ru[index]).strip(), str(ot[index]).strip()]]

            vals.append({
                'msnv': msnv,
                'time_sheet': tmp
            })
        if vals:
            self.create_timesheet_sheet(
                self.start_date, number_days_in_month_selected, vals)
        return {
            'type': 'ir_actions_act_reload_current_view',
        }

    @api.multi
    def create_timesheet_sheet(self, start_date, number_days_in_month_selected, vals):

        for item in vals:
            msnv = item.get('msnv')
            emp = self.env['hr.employee'].sudo().search_read(
                [('code', '=', msnv)], ['id'], limit=1)
            if not emp:
                _logger.warning(
                    'Could not find employee with EMP code: %s' % (msnv))
            time_sheet = item.get('time_sheet')
            if not time_sheet:
                _logger.warning(
                    'Not found time sheet of employee [%s]' % (msnv))

            total_attendance = []
            total_legal_leaves = []
            total_unpaid_leaves = []
            total_ot = []
            daycount = 0
            # Nhan vien chi co 1 hop dong dang open hoac pending ??
            contract = self.env['hr.contract'].sudo().search(
                [('employee_id', '=', emp[0]['id']), ('state', 'in', ['open', 'pending'])])
            temp_date = date(start_date.year, start_date.month, 1)
            for ts in time_sheet:
                daycount += 1
                if daycount > number_days_in_month_selected:
                    break
                date_cursor = temp_date.replace(day=daycount)
                calendars = self.get_time(contract, date_cursor)
                if calendars:
                    total_attendance += [[ts[0], date_cursor, calendars]]
                    total_legal_leaves += [[ts[1], date_cursor, calendars]]
                    total_unpaid_leaves += [[ts[2], date_cursor, calendars]]
                    total_ot +=[[ts[3], date_cursor, '']]
                else:
                    total_ot += [[ts[3], date_cursor, 'is_weekend']]
                # is_legal_leave = self.is_legal_leave(emp[0]['id'], date_cursor)

            self.create_attendance(total_attendance, emp[0]['id'])
            self.create_leaves(total_legal_leaves, emp[0]['id'], "legal")
            self.create_leaves(total_unpaid_leaves, emp[0]['id'],"unpaid")
            self.create_ot(total_ot, emp[0]['id'])
    def is_exist_ot_onday(self, date_cursor, emp_id):
        domain = [('employee_id', '=', emp_id),('request_date_from','<=',date_cursor),('request_date_to','>=',date_cursor)]
        ot = self.env['hr.overtime'].search(domain)
        return ot
    def is_exist_ot_in_calendar(self, date_cursor, emp_id):
        employee = self.env['hr.employee'].browse(emp_id)
        if employee.resource_calendar_id.apply_overtime:
            overtimes = employee.resource_calendar_id.overtime_ids.filtered(lambda r: int(r.dayofweek) == date_cursor.weekday())
            return sorted(overtimes,key= lambda x : x.hour_from)
        return False
    def create_ot_with_exist_in_calendar(self, emp_id, overtimes_in_calendar, ot_time_timesheet, date_cursor, type):
        print("a")
        time_in_calendar = self.sum_time_worked_from_calendars(overtimes_in_calendar)
        time_ot = min(time_in_calendar, float(ot_time_timesheet))
        for calendar in overtimes_in_calendar:
            time_work_session = calendar.hour_to - calendar.hour_from
            if time_ot > 0:
                if time_ot <= time_work_session:
                    self.create_ot_each_one(
                        emp_id, time_ot, calendar.hour_from, date_cursor, type)
                else:
                    self.create_ot_each_one(
                        emp_id, time_work_session, calendar.hour_from, date_cursor, type)
                    time_ot -= time_work_session
        return 0
    def get_key_from_float(self, number):
        if number % 1 != 0:
            return -1*(int(number + 1))
        return int(number)
    def create_ot_each_one(self, emp_id, time_create, hour_from, date_cursor, type):
        hour_to = hour_from + time_create
        hr_overtime = self.env['hr.overtime']
        employee = self.env['hr.employee'].browse(emp_id)
        hour_from = abs(hour_from) - 0.5 if hour_from < 0 else hour_from
        hour_to = abs(hour_to) - 0.5 if hour_to < 0 else hour_to
        request_hour_from = self.get_key_from_float(hour_from)
        request_hour_to = self.get_key_from_float(hour_to)
        if type == 'WEEKEND':
            type_ot = self.env['hr.overtime.type'].search_read(
                    [('is_weekend', '=', True)], ['id'], limit=1)
        elif type == 'HOLIDAY':
            type_ot = self.env['hr.overtime.type'].search_read(
                    [('is_holiday', '=', True)], ['id'], limit=1)
        else:
            type_ot = self.env['hr.overtime.type'].search_read(
                    [('is_weekend', '=', False),('is_holiday','=', False)], ['id'], limit=1)
        values = {
                "employee_id": emp_id,
                "request_hour_from": str(request_hour_from),
                "request_hour_to": str(request_hour_to),
                "date_from": timezone_conversion(datetime(date_cursor.year,date_cursor.month,date_cursor.day, int(hour_from), int((hour_from%1)*60)), self, convert_to="to_utc"),
                "date_to": timezone_conversion(datetime(date_cursor.year,date_cursor.month,date_cursor.day, int(hour_to), int((hour_to%1)*60)), self, convert_to="to_utc"),
                "request_date_from": timezone_conversion(datetime(date_cursor.year,date_cursor.month,date_cursor.day, int(hour_from), int((hour_from%1)*60)), self, convert_to="to_utc"),
                "request_date_to": timezone_conversion(datetime(date_cursor.year,date_cursor.month,date_cursor.day, int(hour_to), int((hour_to%1)*60)), self, convert_to="to_utc"),
                "overtime_status_id": type_ot[0]['id'],
                "calendar_id": employee.resource_calendar_id.id,
                "department_id": employee.department_id.id,
                "number_of_hours": hour_to - hour_from,
                "is_imported":True,
                "state":"validate"
                }
        hr_temp = hr_overtime.create(values)
        hr_temp.onchange_start_date_end_date()
        

    def create_ot(self, total_ot, emp_id):
        for ot in total_ot:
            overtimes_exist_onday = self.is_exist_ot_onday(ot[1],emp_id)
            overtimes_in_calendar = self.is_exist_ot_in_calendar(ot[1], emp_id)
            if not overtimes_exist_onday and ot[0] != '0' and ot[0]:
                is_holiday = self.is_holiday(ot[1])
                if overtimes_in_calendar:
                    if is_holiday:
                        self.create_ot_with_exist_in_calendar(emp_id, overtimes_in_calendar, ot[0], ot[1],'HOLIDAY')
                    elif ot[2] == 'is_weekend':
                        self.create_ot_with_exist_in_calendar(emp_id, overtimes_in_calendar, ot[0], ot[1],'WEEKEND')
                    else:
                        self.create_ot_with_exist_in_calendar(emp_id, overtimes_in_calendar, ot[0], ot[1],'WEEKDAY')
        return True
    def create_ot_with_calendar_and_holiday(self):
        return 0
    def exist_leave_on_day(self, date_cursor, emp_id):
        domain = [('employee_id', '=', emp_id)]
        leaves = self.env['hr.leave'].search(domain)
        if leaves:
            leaves = leaves.filtered(
                lambda x: x.date_from.date() <= date_cursor <= x.date_to.date())
            return sorted(leaves, key=lambda x: x.date_from)
        else:
            return False

    def sum_time_worked_from_calendars(self, calendars):
        return sum(x.hour_to - x.hour_from for x in calendars)

    def convert_date_to_datetime_utc(self, date_cursor, hour):
        date_temp = datetime(
            year=date_cursor.year, month=date_cursor.month, day=date_cursor.day, hour=int(hour))
        return timezone_conversion(date_temp, self, convert_to="to_utc")

    def create_leave_not_exist_each_one(self, date_cursor, emp_id, calendars, time_leave, type):
        total_time = self.sum_time_worked_from_calendars(calendars)
        hr_leave = self.env['hr.leave']
        start_hour_calendar = calendars[0].hour_from
        end_hour_calendar_in_session = calendars[0].hour_to
        end_hour_calendar_in_day = calendars[-1].hour_to
        values = self.get_values(emp_id, date_cursor,type)
        values.update({"date_from": self.convert_date_to_datetime_utc(
            date_cursor, start_hour_calendar)})
        if total_time <= float(time_leave):
            values.update({
                "request_date_to": date_cursor,
                "date_to": self.convert_date_to_datetime_utc(date_cursor, end_hour_calendar_in_day),
            })
        else:
            values.update({
                "request_date_from_period": "am",
                "request_unit_half": True,
                "date_to": self.convert_date_to_datetime_utc(date_cursor, end_hour_calendar_in_session),

            })
        hr_leave_temp = hr_leave.create(values)
        hr_leave_temp.state = "validate"

    def create_leave(self, date_cursor, emp_id, calendars, time_leave, type):
        exist_leave_on_day = self.exist_leave_on_day(date_cursor, emp_id)
        if not exist_leave_on_day:
            self.create_leave_not_exist_each_one(
                date_cursor, emp_id, calendars, time_leave, type)
        else:
            self.create_leave_exist(
                exist_leave_on_day, date_cursor, emp_id, calendars, time_leave, type)

    def get_values(self, emp_id, date_cursor, type):
        employee = self.env['hr.employee'].browse(emp_id)
        values = {"employee_id": emp_id,
                  "holiday_type": "employee",
                  "department_id": employee.department_id.id,
                  "is_imported": True,
                  "request_date_from": date_cursor,
                  }
        if type == "legal":
            values.update(
                {"holiday_status_id": self.env.user.company_id.legal_leave.id})
        elif type == "unpaid":
            values.update(
                {"holiday_status_id": self.env.user.company_id.unpaid_leave.id})
        return values

    def create_leave_exist(self, exist_leave_on_day, date_cursor, emp_id, calendars, time_leave, type):
        total_time = self.sum_time_worked_from_calendars(calendars)
        hr_leave = self.env['hr.leave']
        time_leave_exist = sum(
            x.date_to.hour - x.date_from.hour for x in exist_leave_on_day)
        values = self.get_values(emp_id, date_cursor,type)
        if len(exist_leave_on_day) == 1 and exist_leave_on_day[0].request_unit_half and total_time >= float(time_leave) and float(time_leave) > time_leave_exist:
            if exist_leave_on_day[0].request_date_from_period == 'am':
                start_hour_calendar = calendars[-1].hour_from
                end_hour_calendar_in_session = calendars[-1].hour_to
                values.update({"request_date_from_period": "am"})
            else:
                start_hour_calendar = calendars[0].hour_from
                end_hour_calendar_in_session = calendars[0].hour_to
                values.update({"request_date_from_period": "pm"})
            values.update({
                "date_from": self.convert_date_to_datetime_utc(date_cursor, start_hour_calendar),
                "date_to": self.convert_date_to_datetime_utc(date_cursor, end_hour_calendar_in_session),
                "request_unit_half": True,

            })
            hr_leave_temp = hr_leave.create(values)
            hr_leave_temp.state = "validate"

    def create_leaves(self, total_legal_leaves, emp_id, type):
        if type == "unpaid":
            print("a")
        for legal_leave in total_legal_leaves:
            if legal_leave[0] == '0' or not legal_leave[0]:
                continue
            else:
                self.create_leave(
                    legal_leave[1], emp_id, legal_leave[2], legal_leave[0], type)

    def convert_hour_to_hour_minutes(self, hour):
        return int(hour), int((hour % 1) * 0.6)

    def create_attendance_not_exist_each_one(self, emp_id, time_work, time_start, date_cursor):
        hr_attendance = self.env['hr.attendance']
        check_out_hour, check_out_minute = self.convert_hour_to_hour_minutes(
            time_start + time_work)
        check_in_hour, check_in_minute = self.convert_hour_to_hour_minutes(
            time_start)
        check_out = datetime(date_cursor.year, date_cursor.month,
                             date_cursor.day, check_out_hour, check_out_minute, 0, 0)
        check_in = datetime(date_cursor.year, date_cursor.month,
                            date_cursor.day, check_in_hour, check_in_minute, 0, 0)
        check_in = timezone_conversion(check_in, self, convert_to="to_utc")
        check_out = timezone_conversion(check_out, self, convert_to="to_utc")
        values = {'employee_id': emp_id, 'check_in': check_in,
                  'check_out': check_out, 'is_imported': True}
        hr_attendance.create(values)

    def create_attendance_not_exist(self, emp_id, calendars, time_work_timesheet, date_cursor):
        total_time = sum_time_worked_from_calendars(calendars)
        # Kiem tra du lieu nhap vao cua user co dung hay k
        time_working = min(total_time, time_work_timesheet)
        for calendar in calendars:
            time_work_session = calendar.hour_to - calendar.hour_from
            if (time_working <= time_work_session) and time_working > 0:
                self.create_attendance_not_exist_each_one(
                    emp_id, time_working, calendar.hour_from, date_cursor)
            else:
                self.create_attendance_not_exist_each_one(
                    emp_id, time_work_session, calendar.hour_from, date_cursor)
                time_working -= time_work_session
    ###############################################

    def get_intersec_2_number(self, start_1, end_1, start_2, end_2):
        if end_2 >= start_1 and start_2 <= end_1 and end_2 > start_2 and end_1 > start_1:
            return min(end_1, end_2) - max(start_1, start_2)
        else:
            return False

    def get_hour_of_datime(self, date_cursor):
        a = timezone_conversion(date_cursor, self, convert_to="user_tz")
        return a.hour+a.minute/60.0

    def create_attendance_exist(self, emp_id, calendars, time_work_timesheet, date_cursor, attendances_exist):

        time_work_on_day = 0
        check_calendars = [0 for _ in calendars]
        for index, calendar in enumerate(calendars):
            for attendance in attendances_exist:
                check_in = self.get_hour_of_datime(attendance.check_in)
                check_out = self.get_hour_of_datime(attendance.check_out)
                if check_in and check_out:
                    time_intersec = self.get_intersec_2_number(
                        check_in, check_out, calendar.hour_from, calendar.hour_to)
                    if time_intersec:
                        time_work_on_day += time_intersec
                        check_calendars[index] = 1
        if time_work_timesheet > time_work_on_day:
            time_create = time_work_on_day
            for index, check_calendar in enumerate(check_calendars):
                if time_work_timesheet - time_create <= 0:
                    break
                if not check_calendar:
                    time_create = min(time_work_timesheet - time_work_on_day,
                                      calendars[index].hour_to - calendars[index].hour_from)
                    self.create_attendance_not_exist_each_one(
                        emp_id, time_create, calendars[index].hour_from, date_cursor)
                    time_work_timesheet -= time_create

    def create_attendance(self, total_attendance, emp_id):
        for attendance_timesheet in total_attendance:
            time_work_timesheet = int(float(attendance_timesheet[0]))
            calendars = attendance_timesheet[2]
            attendances_exist = self.get_attendances_exist(
                emp_id, attendance_timesheet[1])
            if not attendances_exist:
                self.create_attendance_not_exist(
                    emp_id, calendars, time_work_timesheet, attendance_timesheet[1])
            else:
                self.create_attendance_exist(
                    emp_id, calendars, time_work_timesheet, attendance_timesheet[1], attendances_exist)

    def get_attendances_exist(self, emp_id, date_cursor):
        attendances = self.env['hr.attendance'].search(
            [('employee_id', '=', emp_id)])
        if attendances:
            attendances = attendances.filtered(
                lambda x: x.check_in.date() == date_cursor)
            return sorted(attendances, key=lambda x: x.check_in)
        return attendances

    # Ham nay da chay

    def get_time(self, contract, date_cursor):
        calendars = contract.resource_calendar_id.attendance_ids.filtered(
            lambda r: int(r.dayofweek) == date_cursor.weekday())
        return sorted(calendars, key=lambda x: x.hour_from)

    def is_holiday(self, date_cursor):
        holidays = self.env['hr.holiday'].search(
            [('activity_state', '=', 'confirm')])
        valid_holiday = self.check_valid_holiday(holidays, date_cursor)
        if valid_holiday:
            return valid_holiday
        return False

    def check_valid_holiday(self, holidays, date_cursor):
        for holiday in holidays:
            if holiday.request_unit == 'half_day':
                if holiday.date_from.date() == date_cursor:
                    return holiday
            else:
                if holiday.date_from.date() <= date_cursor <= holiday.date_to.date():
                    return holiday
        return False