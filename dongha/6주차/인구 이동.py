import sys
import collections
def input() : return sys.stdin.readline().rstrip()

def main() :
    # N : 땅 가로세로 크기,
    # L, R : 국경 사이의 두 국가의 인구수 차이가 L 이상 R 이하일 때 연합으로 취급
    N, L, R = map(int, input().split())

    # 초기 땅 위의 인구수 입력받기
    land = []
    for _ in range(N):
        new_line = list(map(int, input().split()))
        land.append(new_line)
    
    # 인구이동이 일어난 숫자
    answer = 0
    while True:
        # 동맹들의 집합을 모아놓는 리스트
        aliance_set_list = [] 
        # 각 동맹 번호를 매겨놓은 2차원 배열. -1이면 아직 동맹처리 안한거
        aliance_check = [[-1] * N for _ in range(N)]

        # 동맹 번호는 0번부터 시작
        aliance_number = 0
        # 땅 전부 순회하면서
        for y in range(N):
            for x in range(N):
                # 지금 칸은 아직 동맹 처리 안했다면
                if aliance_check[y][x] == -1:
                    # 너비 우선 탐색을 위한 큐
                    queue = collections.deque()
                    queue.append((y,x))
                    aliance_check[y][x] = aliance_number
                    aliance_set_list.append(set()) # 동맹 집합 리스트에 집합 하나 추가
                    aliance_set_list[aliance_number].add((y,x)) # 동맹집합에 지금 칸 추가
                    
                    # 너비 우선 탐색 for문 간소화용 오프셋 리스트 
                    POS_OFFSET = [(-1, 0), (+1, 0), (0, -1), (0, +1)]
                    while queue:
                        row, col = queue.popleft()
                        for offset in POS_OFFSET:
                            new_row = row + offset[0]
                            new_col = col + offset[1]
                            if (0 <= new_row < N) and (0 <= new_col < N):
                                if aliance_check[new_row][new_col] == -1:
                                    if L <= abs(land[row][col] - land[new_row][new_col]) <= R:
                                        aliance_check[new_row][new_col] = aliance_number
                                        aliance_set_list[aliance_number].add((new_row,new_col))
                                        queue.append((new_row,new_col))    
                    aliance_number += 1
        
        # 순회 다 끝났는데 동맹 집합 리스트 길이가 N*N이라면 => 더 이상 동맹 안만들어지면 break
        if len(aliance_set_list) == N*N:
            break
        
        # 그거 아니면 인구이동 실시
        answer += 1 # 인구이동 카운트 증가
        
        # 먼저 동맹별 인구를 구한다.
        population_list = [] # 동맹별 인구수
        for one_aliance in aliance_set_list:
            pop_sum = 0
            for one_cell in one_aliance:
                y, x = one_cell
                pop_sum += land[y][x]
            population_list.append(pop_sum // len(one_aliance)) # "편의상 소수점은 버린다."
        
        # 인구이동을 실제로 실시 -> population_list를 순람표로 사용하여 check리스트에 따라 인구 변화
        for y in range(N):
            for x in range(N):
                a_number = aliance_check[y][x]
                land[y][x] = population_list[a_number]
    # end while
    
    print(answer)
    return
#####
main()