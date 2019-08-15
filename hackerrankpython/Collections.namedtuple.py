from collections import namedtuple

N = int(input())
Any_order=input().split()
for i in range(len(Any_order)):
    if Any_order[i] == "MARKS":
        MARKS_index = i 
total = 0
for i in range(N):
    new_Student = input().split()
    total += int(new_Student[MARKS_index])

print(float(total/N))
