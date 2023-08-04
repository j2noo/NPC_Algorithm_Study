R, C, N = map(int, input().split())
arr = [list(input()) for _ in range(R)]
beforeArr = [["." for _ in range(C)] for _ in range(R)]
bombArr = [["O" for _ in range(C)] for _ in range(R)]

dy = [-1, 0, 1, 0, 0]
dx = [0, 1, 0, -1, 0]


for time in range(1, N):
    if time % 2 == 0:
        continue

    for i in range(R):
        for j in range(C):
            bombArr[i][j] = "O"

    # 폭발검사
    for i in range(R):
        for j in range(C):
            # 원래 폭탄이 없는칸이었으면 패스
            if arr[i][j] == ".":
                continue

            # 원래 폭탄이 존재하던 칸 = 터져야 하는 칸
            for dir in range(5):
                newR = i + dy[dir]
                newC = j + dx[dir]
                if newR < 0 or newC < 0 or newR >= R or newC >= C:
                    continue
                bombArr[newR][newC] = "."

    for i in range(R):
        for j in range(C):
            arr[i][j] = bombArr[i][j]


for i in range(R):
    for j in range(C):
        if N % 2 == 0:
            arr[i][j] = "O"
        print(arr[i][j], end="")
    print()
