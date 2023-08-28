from collections import deque


N, M = map(int, input().split())
incidence_li = [[] for _ in range(N + 1)]

# print(incidence_li)
for _ in range(M):
    A, B = map(int, input().split())
    incidence_li[A].append(B)
    incidence_li[B].append(A)


def bfs(node):
    global visited
    depth = 1
    queue = deque()

    queue.append(node)
    visited[node] = depth

    while len(queue) > 0:
        qs = len(queue)
        for i in range(qs):
            pop = queue.popleft()
            for inci in incidence_li[pop]:
                if visited[inci] == -1:
                    queue.append(inci)
                    visited[inci] = depth
        depth += 1


ansIdx = -1
ans = float("INF")
for i in range(1, N + 1):
    visited = [-1] * (N + 1)
    bfs(i)
    sum = 0
    for j in range(1, N + 1):
        sum += visited[j]

    if ans > sum:
        ans = sum
        ansIdx = i

print(ansIdx)
