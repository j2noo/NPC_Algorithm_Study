import sys

S = sys.stdin.readline().rstrip()
T = sys.stdin.readline().rstrip()

ret = 0
while T != "" :
    if T[-1] == 'A':
        T = T[:-1]
    else :
        T = T[:-1][::-1]
    if T == S:
        ret = 1
        break
print(ret)
        
