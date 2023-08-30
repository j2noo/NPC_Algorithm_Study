import itertools

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
chicken_li = []
home_li = []
ans = float("INF")

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            home_li.append([i, j])
        if arr[i][j] == 2:
            chicken_li.append([i, j])
chicken_cnt = len(chicken_li)

# 전체중 M개의 치킨집만 고르기
select_li = list(itertools.combinations(range(chicken_cnt), M))

# 치킨집의 combimations 고름
for select in select_li:
    # print(select)
    chicken_dist = 0

    # 모든 집에 대해 최소 치킨거리
    for home in home_li:
        home_dist = float("INF")
        # 선택한 치킨집들의 치킨거리
        for selected_chicken in select:
            chicken_coord = chicken_li[selected_chicken]

            home_dist = min(
                home_dist,
                abs(chicken_coord[0] - home[0]) + abs(chicken_coord[1] - home[1]),
            )

        chicken_dist += home_dist

    ans = min(ans, chicken_dist)
print(ans)
