import sys

sys.setrecursionlimit(10**5)
n = int(input())

arr = []
dp = [[-1, -1] for _ in range(n + 1)]

for i in range(n):
    arr.append(int(input()))


# nth에서 마신 최대 포도주
def solve(nth, prev):
    if nth >= n:
        return 0
    if dp[nth][prev] != -1:
        return dp[nth][prev]
    # 이전에 안마셨다면
    if prev == 0:
        # 지금 마시거나, 안마시거나
        dp[nth][prev] = max(solve(nth + 1, 1) + arr[nth], solve(nth + 1, 0))

    # 이전에 마셨다면
    if prev == 1:
        # 지금 마시는데 다음거패스, 안마시거나

        dp[nth][prev] = max(solve(nth + 2, 0) + arr[nth], solve(nth + 1, 0))
    return dp[nth][prev]


print(solve(0, 0))