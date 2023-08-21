dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
ans = 1

# for i in range(R):
#     print(arr[i])

for i in range(R):
    for j in range(C):
        if arr[i][j] == "S":
            for dir in range(4):
                newR = i + dy[dir]
                newC = j + dx[dir]
                if newR < 0 or newR >= R or newC < 0 or newC >= C:
                    continue
                if arr[newR][newC] == "W":
                    ans = 0
                if arr[newR][newC] == ".":
                    arr[newR][newC] = "D"

print(ans)
if ans == 1:
    for i in range(R):
        for j in range(C):
            print(arr[i][j], end="")
        print()
