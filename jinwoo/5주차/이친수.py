N = int(input())

# 0, 1로 끝나는 이친수의 개수
dp = [[0, 0] for i in range(N + 1)]

dp[1] = [0, 1]

for i in range(2, N + 1):
    dp[i][0] += dp[i - 1][0]  # 0으로 끝났으면 0 붙이기
    dp[i][0] += dp[i - 1][1]  # 1으로 끝났으면 0 붙이기
    dp[i][1] += dp[i - 1][0]  # 0으로 끝났으면 1 붙이기


print(dp[N][0] + dp[N][1])
