from collections import deque
import copy
import itertools

N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]
cnt = 0
ans = -1


global copyArr


def bfs(archer):
    global copyArr
    queue = deque()

    visited = [[0] * M for _ in range(N)]
    depth = 1
    queue.append(archer)
    visited[archer[0]][archer[1]] = 1
    while len(queue) > 0 and depth <= D:
        qsize = len(queue)
        for _ in range(qsize):
            pop = queue.popleft()
            if copyArr[pop[0]][pop[1]] == 1:  # 적이면
                return pop
            for dir in range(4):
                newR = pop[0] + dy[dir]
                newC = pop[1] + dx[dir]

                if newR >= N or newR < 0 or newC >= M or newC < 0:
                    continue
                if visited[newR][newC] == 0:
                    queue.append([newR, newC])
                    visited[newR][newC] = 1
        depth += 1
    return -1


def solve(stack):
    global ans
    global copyArr
    copyArr = copy.deepcopy(arr)
    cnt = 0
    archers = [[N - 1, stack[0]], [N - 1, stack[1]], [N - 1, stack[2]]]  # 궁수가 거리 1인 자리

    for _ in range(N):
        availShoot = []
        for archer in archers:
            availShoot.append(bfs(archer))  # 지금 쏘지마

        for shoot in availShoot:
            if shoot == -1:
                continue
            if copyArr[shoot[0]][shoot[1]] == 1:
                copyArr[shoot[0]][shoot[1]] = 0
                cnt += 1
        # 아래로
        for i in range(N - 1, 0, -1):
            copyArr[i] = copyArr[i - 1]
        copyArr[0] = [0] * M

    ans = max(ans, cnt)
    # print(cnt)


def getCombination(next, left):
    if left == 0:
        solve(stack)
        return
    if next >= M:
        return
    # 배치
    stack.append(next)
    getCombination(next + 1, left - 1)
    stack.pop()

    # 미배치
    getCombination(next + 1, left)


# getCombination(0, 3)

nCr = itertools.combinations(range(M), 3)
for li in nCr:
    solve(list(li))

print(ans)
