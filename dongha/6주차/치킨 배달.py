import sys
from itertools import combinations

# 빠른 입력
def input() : return sys.stdin.readline().rstrip()

# 두 튜플(y, x)을 받아 맨해튼 거리 계산하여 반환
def distance(t0, t1):
    return abs(t0[0] - t1[0]) + abs(t0[1] - t1[1])


def main():
    # 초기화용 무한 값
    INF = 9999_9999_9999_9999_9999_9999

    # N : 맵 가로세로 크기, M : 폐업 안시킬 치킨집 갯수(치킨집은 반드시 M보다 많게 존재한다.) 
    N, M = map(int, input().split())

    # 치킨집 좌표 리스트
    fried_chicken_restaurant_array = []
    fcr_array = fried_chicken_restaurant_array
    # 집 좌표 리스트
    home_array = []

    # 빠른 if 분기문을 위한 lookup table같은거 생성
    switch = [None] * 3
    switch[0] = lambda x : None                 # 0이면 빈칸 -> 아무것도 안 함
    switch[1] = lambda x : home_array.append(x) # 1이면 집
    switch[2] = lambda x : fcr_array.append(x)  # 2이면 치킨집

    # 맵을 입력받으면서 1이나 2가 나오면 좌표를 각 리스트에 넣음
    for y in range(N):
        ROW = list(map(int, input().split()))
        for x in range(N):
            switch[ROW[x]]((y, x))
    
    # 가능한 치킨집의 조합을 모두 순회하면서 각 집까지에 이르는 치킨거리를 계산
    # 동시에 치킨거리의 합의 최솟값을 갱신
    min_chicken_distance = INF
    FCR_COMBINATION = combinations(fcr_array, M)
    for fcr_list in FCR_COMBINATION:
        # 각 집별 치킨거리 리스트
        d_list = [INF] * len(home_array)
        # 조합 내 레스토랑별로 순회
        for one_restaurant_pos in fcr_list:
            # 레스토랑 하나당 집 하나씩 순회
            for home_idx in range(len(home_array)):
                d_list[home_idx] = min(
                    d_list[home_idx], 
                    distance(one_restaurant_pos, home_array[home_idx])
                )
        min_chicken_distance = min(min_chicken_distance, sum(d_list))

    # 치킨 거리 최솟값 출력
    print(min_chicken_distance)
    return
#####  
main()