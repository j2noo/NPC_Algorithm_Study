import sys
from itertools import combinations
import collections
import copy

#sys.stdin = open("input.txt", 'r')

# 격자판 행 수 N
# 격자판 열 수 M
# 궁수의 공격 거리 제한(맨해튼 거리) D
# 입력받음
N, M, D = map(int, sys.stdin.readline().split(' '))

# 처음 맵의 상태를 입력받음
MAP_INIT = []
for _ in range(N):
    MAP_INIT.append(list(map(int, sys.stdin.readline().split(' '))))

# 가능한 궁수의 모든 배치 방법
POSSIBLE_ARCHER_POS = combinations(list(range(0, M)), 3)

# 좌, 상, 우 방향
dy = [ 0, -1,  0]
dx = [-1,  0, +1]

# 궁수의 위치, 맵정보, 위치제한을 넣었을 떄
# 궁수가 제일 먼저 공격하는 적의 위치의 좌표를 (y,x)형식으로 반환하는 함수
# 못찾으면 None 반환
def retArcherAttackPos(x_pos, arg_map) :
    global N, M, D
    queue = collections.deque()
    queue.append((N-1,x_pos, 1))
    while queue:
        y, x, d = queue.popleft()
        if d > D :
            return None
        if arg_map[y][x] == 1:
            return (y, x)
        for i in range(3):
            new_y = y + dy[i]
            new_x = x + dx[i]
            condition = ( 0 <= new_x < M ) and ( 0 <= new_y < N )
            if condition :
                queue.append((new_y, new_x, d+1))

# 맵 상의 적들을 한 칸 앞으로 이동시킨 새로운 맵 반환
def enemyAdvance(arg_map):
    new_map = []
    new_map.append([0 for _ in range(M)]) # 처음 요소는 0으로 채운거
    for i in range(0, N-1): #마지막 행 빼고 나머지는 그대로 이어붙임 -> 한 칸 전진한듯이 보이게 됨
        new_map.append(arg_map[i])
    return new_map

# 맵 상에 적이 더 이상 없는지 확인함
def isMapEmpty(arg_map):
    for y in range(len(arg_map)):
        for x in range(len(arg_map[0])):
            if arg_map[y][x] == 1:
                return False
    return True

# 디버그용
def printMap(arg_map):
    print('------------------')
    for i in arg_map:
        print(i)
# 1. 가능한 궁수의 모든 경우를 순회하면서
# 2. isMapEmpty로 맵이 비었는지 계속 확인하면서
# 3. retArcherAttackPos함수를 사용하면서 + enemyAdvance로 맵을 한 칸 땡김
answer = 0
for archery_positions in POSSIBLE_ARCHER_POS:
    a0, a1, a2 = archery_positions
    #MAP_TMP = MAP_INIT[:] 
    MAP_TMP = copy.deepcopy(MAP_INIT)
    ret = 0
    while not isMapEmpty(MAP_TMP):
        #printMap(MAP_TMP)
        attack_set = set()
        attack_set.add(retArcherAttackPos(a0, MAP_TMP))
        attack_set.add(retArcherAttackPos(a1, MAP_TMP))
        attack_set.add(retArcherAttackPos(a2, MAP_TMP))
        for e in attack_set:
            if e != None:
                r, c = e
                MAP_TMP[r][c] = 0
                ret += 1
        MAP_TMP = enemyAdvance(MAP_TMP)
    answer = max(answer, ret)
print(answer)