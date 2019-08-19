from collections import deque
N = int(input())
d = deque()
for i in range(N):
    name = input().split()
    if name[0] == 'append':
        d.append(name[1])
    elif name[0] == "pop":
        d.pop()
    elif name[0] == "popleft":
        d.popleft()
    else:
        d.appendleft(name[1])

print(' '.join(d))
