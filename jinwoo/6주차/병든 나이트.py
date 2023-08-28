N, M = map(int, input().split())

# 높이가 3이상
if N >= 3 and M >= 7:
    ans = M - 2
elif N >= 3 and M < 7:
    ans = min(4, M)

# 높이가 2
elif N == 2:
    ans = min(4, (M + 1) // 2)

# 높이가 1
else:
    ans = 1

print(ans)
