import sys
import collections
import io
sio = io.StringIO()

#sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())

TOWN_MAP = []
TOWN_MAP.append([0] * (N+2))
for _ in range(N):
    TOWN_MAP.append([0] + list(map(int, sys.stdin.readline().rstrip())) + [0])
TOWN_MAP.append([0] * (N+2))


# 안에 넣는 요소의 형태는 (y, x)
queue = collections.deque()
ret_list = []
#단지 수
ret = 0

for y in range(1,N+1):
    for x in range(1,N+1):
        num = 0 #단지 내 가구원 수
        if TOWN_MAP[y][x] == 1:
            ret += 1
            queue.append((y, x))
        while queue:
            a, b = queue.popleft()
            if TOWN_MAP[a][b] == 1:
                num += 1
                TOWN_MAP[a][b] = 0
                queue.append((a, b+1))
                queue.append((a, b-1))
                queue.append((a+1, b))
                queue.append((a-1, b))
        if num != 0:
            ret_list.append(num)

sio.write(str(ret))
sio.write('\n')
ret_list.sort()

for i in ret_list:
    sio.write(str(i))
    sio.write('\n')

sys.stdout.write(sio.getvalue())
