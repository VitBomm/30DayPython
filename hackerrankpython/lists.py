if __name__ == '__main__':
    N = int(input())
    listtemp = []
    for i in range(N):
        src = str(input())
        temp = src.split(' ')
        if temp[0] == "insert":
            listtemp.insert(int(temp[1]), int(temp[2]))
        elif temp[0] == "print":
            print([x for x in listtemp])
        elif temp[0] == "remove":
            listtemp.remove(int(temp[1]))
        elif temp[0] == "sort":
            listtemp.sort()
        elif temp[0] == "pop":
            listtemp.pop()
        elif temp[0] == "append":
            listtemp.append(int(temp[1]))
        else:
            listtemp.reverse()
