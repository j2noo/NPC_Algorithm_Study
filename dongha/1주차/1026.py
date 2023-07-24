import sys
#sys.stdin = open("input.txt", 'r')

LENGTH = int(sys.stdin.readline())

A_ARRAY = list(map(int, sys.stdin.readline().split()))
B_ARRAY = list(map(int, sys.stdin.readline().split()))

A_ARRAY.sort()
B_ARRAY.sort(reverse=True)

s = 0
for i in range(LENGTH):
    s+=A_ARRAY[i]*B_ARRAY[i]

sys.stdout.write(str(s))
