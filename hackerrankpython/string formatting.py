n = int(input())
m = len('{0:b}'.format(n))
for i in range(n):
    print('{0}'.format(i+1).rjust(m,' ') +' {0:o}'.format(i+1).rjust(m+1,' ')+' {0:X}'.format(i+1).rjust(m+1,' ')+ '{0:b}'.format(i+1).rjust(m+1,' '))
