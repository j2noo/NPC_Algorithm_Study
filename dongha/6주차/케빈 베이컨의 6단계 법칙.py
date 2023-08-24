import sys
def input() : return sys.stdin.readline().rstrip()

def main():
    # 무한
    INF = 99999999999999999

    # 유저의 수 N, 친구 관계 수 M
    N, M = map(int, input().split())
    
    # 최단거리 테이블 구성
    # 출발\도착  1  2 
    # 1
    # 2
    # 최단거리 테이블 
    # N+1로 하는 이유 : 번호는 1부터 시작 + 인덱스 처리 생략용
    min_distance_table = [[INF] * (N+1) for _ in range(N+1)]

    # 자기 자신으로 향하는 거리는 무조건 0
    for i in range(1, N+1):
        min_distance_table[i][i] = 0

    # 친구관계 입력받음
    for _ in range(M):
        A, B = map(int, input().split())
        min_distance_table[A][B] = 1
        min_distance_table[B][A] = 1

    # 플로이드 워셜 알고리즘 : min(d_ab, d_ak+d_kb)
    for k in range(1, N+1):
        for a in range(1, N+1):
            for b in range(1, N+1):
                min_distance_table[a][b] = min(min_distance_table[a][b], min_distance_table[a][k]+min_distance_table[k][b])
    
    # 케빈 베이컨의 수가 가장 작은 사람 구하기
    min_value = INF
    number = -1
    for row in range(1, N+1):
        tmp_sum = 0
        for col in range(1, N+1):
            if min_distance_table[row][col] < INF:
                tmp_sum += min_distance_table[row][col]
        if min_value > tmp_sum:
            number = row
            min_value = tmp_sum
    
    # 위에서 구한, 케빈 베이컨이 가장 작은 번호 출력
    print(number)
#####
main()