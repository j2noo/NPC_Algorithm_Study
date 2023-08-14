import sys

# N 입력
N = int(sys.stdin.readline())
# 미로 입력
MAZE = tuple(map(int, sys.stdin.readline().rstrip().split()))

# 도달 불능의 기준 :
### 아직 끝이 아닌데 지금 있는 위치가 0
### 예외 - 미로가 1칸짜리일 경우 시작칸이 0이더라도 최대 점프 수는 0이 된다.
###        (시작하자마자 끝이므로)
def isEnd(idx) :
    global MAZE
    return MAZE[idx] == 0

# 체크메이트 판정 :
### 자기 자신의 idx(0부터 시작) + 1 + 자기 칸의 번호 > N이면
### break하고 점프 수 + 1 한 후에 종료
### 이는 마지막번째 그거에서 인덱스 초과가 발생 안하게 하려는 의도도 있다.
def isCheckmate(idx) :
    global MAZE, N
    return (idx + 1 + MAZE[idx]) >= N

# 이동의 기준
### [3]  1  6  3 ... 이래 있다 가정할 때
###     +1 +2 +3 씩 가중치를 둔다.
### 이럼 2  8  6 이래 되는데, 여기서 가중치가 가장 높은 칸을 선택한다.
### 이때 탐색 순서는 뒤에서부터 앞으로 탐색하며, 가중치가 같은 칸이 나왔다면 무시한다.
### (오로지 가중치가 더 높아야 최신화된다.)
### 가중치+번호의 비교를 위한 초기값은 절대 존재할 수 없는 -1 같은걸로 한다.

idx = 0
jump = 0
if len(MAZE) != 1: # 칸이 1칸이라면 시작하자마자 오른쪽 끝이므로 바로 0을 출력하게 만든다.
    while True:
        if isEnd(idx):
            jump = -1
            break
        if isCheckmate(idx):
            jump += 1
            break
        capability = MAZE[idx]
        to_idx = 99999 #초기화용
        score = -1 #초기화용
        for i in range(capability, 0, -1): # i가 가중치 역할도 함
            if MAZE[idx + i] + i > score:
               to_idx =  idx + i
               score = MAZE[idx + i] + i
        idx = to_idx
        jump += 1

sys.stdout.write(str(jump))
