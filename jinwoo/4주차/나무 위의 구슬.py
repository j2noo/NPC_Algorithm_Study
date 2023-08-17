import sys

N = int(sys.stdin.readline())

child = [[-1, -1] for _ in range(N + 1)]


for i in range(1, N + 1):
    left, right = map(int, sys.stdin.readline().split())
    child[i][0] = left
    child[i][1] = right

K = int(sys.stdin.readline())
currNode = 1

while 1:
    if child[currNode][0] == -1 and child[currNode][1] == -1:
        break
    elif child[currNode][0] == -1:  # 오른쪽 자식만 존재
        currNode = child[currNode][1]
    elif child[currNode][1] == -1:  # 왼쪽 자식만 존재
        currNode = child[currNode][0]
    else:
        # 짝수이면 오른쪽
        if K % 2 == 0:
            currNode = child[currNode][1]
            K = int(K // 2)
        # 홀수이면 왼쪽
        else:
            currNode = child[currNode][0]
            K = int((K + 1) // 2)
print(currNode)
