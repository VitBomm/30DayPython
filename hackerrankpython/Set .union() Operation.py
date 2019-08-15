if __name__ == "__main__":
    a = int(input())
    array_a = set(map(int, input().split()))
    b = int(input())
    array_b = set(map(int, input().split()))

    print(len(array_a.union(array_b)))
