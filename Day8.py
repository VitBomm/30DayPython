PhoneBook = {}
n = int(input())
for i in range(n):
    key,value = input().split()
    PhoneBook[key] = value

while(True):
    try:
        k = input()
        if k in PhoneBook:
            print(k+"="+PhoneBook[k])
        else:
            print("Not found")
    except EOFError:
        break


