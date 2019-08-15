class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = -float('Inf')
    def computeDifference(self):
        temp = sorted(self.__elements)
        self.maximumDifference = temp[-1] - temp[0]

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)