def print_rangoli(size):
    n = size
    left = (n-1)*2
    
    def generatetop(number,a):
        temp = '-'*a
        num_char = 96 + n
        for _ in range(number):
            temp += (chr(num_char) + '-')
            num_char -= 1
        temp += chr(num_char)
        for _ in  range(number):
            num_char += 1
            temp += '-' + chr(num_char)

        temp += '-' * a
        return temp

    def generatemid(number):
        temp =''
        num_char = 96 + n
        for _ in range(number):
            temp += (chr(num_char) + '-')
            num_char -= 1
        temp += chr(num_char)
        for _ in  range(number):
            num_char += 1
            temp += '-' + chr(num_char)
        return temp
    # bot
    def generatebot(number,a):
        temp = '-'*a
        num_char = 96 + n
        for _ in range(number):
            temp += (chr(num_char) + '-')
            num_char -= 1
        temp += chr(num_char)
        for _ in  range(number):
            num_char += 1
            temp += '-' + chr(num_char)

        temp += '-' * a
        return temp

    for i in range(n-1):
        print(generatetop(i,left))
        left -= 2

    print(generatemid(n-1))

    for i in range(n-1):
        left += 2
        print(generatebot(n-2-i,left))



if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
