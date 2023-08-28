import sys

sys.setrecursionlimit(10**5)

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


N, L, R = map(int, input().split())

arr = list(list(map(int, input().split())) for _ in range(N))
visited = [[0] * N for _ in range(N)]

team = []
teamSum = 0
ans = 0


# 연합 찾기
def dfs(i, j):
    global teamSum, team
    team.append([i, j])
    teamSum += arr[i][j]
    visited[i][j] = 1
    for dir in range(4):
        newR = i + dy[dir]
        newC = j + dx[dir]
        if newR < 0 or newR >= N or newC < 0 or newC >= N:
            continue
        if visited[newR][newC] == 1:
            continue
        if L <= abs(arr[i][j] - arr[newR][newC]) <= R:
            dfs(newR, newC)


while 1:
    teamCnt = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                dfs(i, j)
                teamCnt += 1
                for ii, jj in team:
                    arr[ii][jj] = int(teamSum / len(team))
                team.clear()
                teamSum = 0
    if teamCnt == N * N:
        break
    ans += 1

print(ans)
