n, m = map(int,input().split())

left = (m-3)//2

def center(length):
    temp = '.|.'
    for _ in range(length):
        temp += '.|.'
        temp = '.|.' + temp
    return temp


# top door mat
for i in range(n//2):
    print('-'*left + center(i) + '-'*left)
    left -= 3

center_half_length = (m-7)//2
# center door mat

print('-'*center_half_length + 'WELCOME' + '-'*center_half_length)

#bot door mat

for i in range(n//2):
    left += 3
    print('-'*left + center((n//2 - 1)-i) + '-'*left)
