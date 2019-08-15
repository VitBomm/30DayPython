T = int(input())

for i in range(T):
    a,b = input().split()
    try:
        c = int(a)
    except ValueError as e:
        print("Error Code: invalid literal for int() with base 10: '{0}'".format(a))
        continue
    try:
        d = int(b)
    except ValueError as e:
        print("Error Code: invalid literal for int() with base 10: '{0}'".format(b))
        continue
    try:
        print(c//d)
    except ZeroDivisionError as e:
        print("Error Code: integer division or modulo by zero")