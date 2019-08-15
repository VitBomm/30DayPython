from collections import Counter
n = input()
listA = list(map(int,input().split()))
newlist = Counter(listA)
print(newlist.most_common()[-1][0])