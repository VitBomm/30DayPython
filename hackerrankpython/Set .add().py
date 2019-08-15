# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    n = int(input())
    array = {input() for _ in range(n)}
    print(len(array))
