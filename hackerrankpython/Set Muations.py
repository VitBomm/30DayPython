n = input()
setA = set(map(int,input().split()))
number_of_set = int(input())
for i in range(number_of_set):
    name_operation, lenght= input().split()
    other_set = set(map(int, input().split()))
    if name_operation == "intersection_update":
        setA.intersection_update(other_set)
        continue
    if name_operation == "update":
        setA.update(other_set)
        continue
    if name_operation == "symmetric_difference_update":
        setA.symmetric_difference_update(other_set)
        continue
    if name_operation == "difference_update":
        setA.difference_update(other_set)
        continue

print(sum(setA))


