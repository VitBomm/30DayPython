T = int(input())
for i in range(T):
    a = input()
    print("".join(a[::2])+ " "+ "".join(a[1::2]))
