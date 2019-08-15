n = int(input())
s = set(map(int, input().split()))

N = int(input())

for _ in range(N):
    temp = input()
    if temp.startswith('pop'):
        s.pop()
    elif temp.startswith('remove'):
        s.remove(int(temp[7::]))
    else:
        s.discard(int(temp[8::]))


print(sum(s))
