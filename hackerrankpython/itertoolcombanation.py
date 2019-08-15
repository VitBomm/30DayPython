from itertools import combinations

str_temp, number = input().split()

[ print(''.join(x))for index in range(int(number)) for x in list(combinations(''.join(sorted(str_temp)),index+1))]
