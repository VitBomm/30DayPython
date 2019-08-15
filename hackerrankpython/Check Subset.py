T = int(input())
for i in range(T):
    a = input()
    setA = set(map(int,input().split()))
    b = input()
    setB = set(map(int,input().split()))
    if setA.issubset(setB): print("True")
    else: print("False")
