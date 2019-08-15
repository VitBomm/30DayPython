from collections import OrderedDict
n = int(input())
dictionary = OrderedDict()
for i in range(n):
    Name_Food = list(map(str,input().split()))
    key = " ".join(Name_Food[0:(len(Name_Food)-1)])
    value = int(Name_Food[-1])
    if key in dictionary:
        dictionary[key] += value
    else:
        dictionary[key] = value

for key, value in dictionary.items():
    print("{0} {1}".format(key, value))