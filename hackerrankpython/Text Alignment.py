#Replace all ______ with rjust, ljust or center.

thickness = int(input()) #This must be an odd number
c = 'H'
#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1, ' ')+c+(c*i).ljust(thickness-1,' '))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).rjust(thickness + ((thickness)//2),' ') + (' '*thickness*3) + (c*thickness).ljust(thickness,' '))


#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).rjust(thickness*5 + thickness//2,' '))
#
#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).rjust(thickness + (thickness//2),' ') + (' '*thickness*3) + (c*thickness).ljust(thickness,' '))
# #Bottom Cone
for i in range(thickness):
    print(' '*(thickness*3 + thickness-1) + (c*(thickness-i-1)).rjust(thickness,' ')+c+(c*(thickness-i-1)).ljust(thickness,' '))
