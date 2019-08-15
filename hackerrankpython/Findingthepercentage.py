if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        intputArray = input().split()
        scores =list(map(float, intputArray[1:]))
        student_marks[intputArray[0]] = sum(scores) / len(scores)

    print("{0:.2f}".format(student_marks[input()]))
