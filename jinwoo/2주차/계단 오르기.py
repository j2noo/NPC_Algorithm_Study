n = int(input())
arr = [-1]
for i in range(n):
    arr.append(int(input()))
dp = [-1] * 10000


# n번째 계단을 밟을 때 얻을 수 있는 최대 점수
def solve(n):
    if n == 1:
        return arr[1]
    elif n == 2:
        return arr[1] + arr[2]
    elif n == 3:
        return max(arr[1] + arr[3], arr[2] + arr[3])

    # 계산결과가 존재하면
    if dp[n] != -1:
        return dp[n]

    dp[n] = max(solve(n - 2), solve(n - 3) + arr[n - 1]) + arr[n]

    return dp[n]


print(solve(n))
