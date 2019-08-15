setA = set(map(int,input().split()))

n = int(input())
result = "True"
for i in range(n):
    otherset = set(map(int,input().split()))
    if not otherset.issubset(setA):
        result = "False"
        break

print(result)
