n = input()
list_temp = list(map(int,input().split()))
print(all([any(list(map(lambda x: list(str(x)) == list(str(x))[::-1], list_temp)))]+list(map(lambda x: x >= 0, list_temp))))
