N = int(input())

# 지금까지 놓은 좌표
stack = []
cnt = 0


# n번째 줄에 퀸을 놓기
def solve(n):
    global cnt
    if n == N:
        cnt += 1
        return
    for i in range(N):
        newQueen = [n, i]  # 퀸의 좌표
        isPossible = 1
        for queen in stack:
            # 우상단으로 같음
            if queen[0] + queen[1] == n + i:
                isPossible = 0
                break
            # 좌하단으로 같음
            if queen[0] - n == queen[1] - i:
                isPossible = 0
                break
            # 세로로 같음
            if queen[1] == i:
                isPossible = 0
                break

        if isPossible == 1:
            stack.append(newQueen)
            solve(n + 1)
            stack.pop()


solve(0)

print(cnt)
