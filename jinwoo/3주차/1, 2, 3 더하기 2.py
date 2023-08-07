N, K = map(int, input().split())
stack = []
cnt = 0


def createAll(n):
    global cnt
    if n == 0:
        cnt += 1
        if cnt == K:
            for i in range(len(stack) - 1):
                print(stack[i], end="+")
            print(stack[len(stack) - 1])
            return
    if n >= 1:
        stack.append(1)
        createAll(n - 1)
        stack.pop()
    if n >= 2:
        stack.append(2)
        createAll(n - 2)
        stack.pop()
    if n >= 3:
        stack.append(3)
        createAll(n - 3)
        stack.pop()


createAll(N)
if cnt < K:
    print(-1)
