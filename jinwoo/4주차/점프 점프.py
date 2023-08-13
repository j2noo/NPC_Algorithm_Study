N = int(input())
arr = list(map(int, input().split()))
dp = [-1] * 1001


# n번쨰 칸에서 끝까지 갈 수 있는 최소횟수
def solve(n):
    if dp[n] != -1:
        return dp[n]

    if arr[n] + n >= N - 1:
        return 1

    minJump = float("inf")
    for i in range(1, arr[n] + 1):
        minJump = min(minJump, solve(n + i) + 1)
    dp[n] = minJump
    return dp[n]


if solve(0) == float("inf"):
    print("-1")
elif N == 1:
    print(0)
else:
    print(solve(0))
