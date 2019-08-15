# temp_str, i = list(input()), int(input())
# n = len(temp_str)
#
# m = n//i if n % i == 0 else n//i + 1
# print(m)
#
# for _ in range(m):
#     print(''.join(temp_str[(_*i):i*(_+1)]))
#
import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


#ABCDEFGHIJKLIMNOQRSTUVWXYZ
#4
