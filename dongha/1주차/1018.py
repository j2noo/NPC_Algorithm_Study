import sys
#sys.stdin = open("input.txt", "r")

# 체스판 높이와 너비 받기
HEIGHT, WIDTH = map(int, sys.stdin.readline().split(' '))

# 체스판 전체를 입력 파일에서 모조리 받아온 후
# 엔터 단위로 나눠서 2차원으로 만들기
input_list = sys.stdin.read().split('\n')
# EOF 있으면 제거
if(input_list[-1] == ""): input_list.pop()

# 체스판1
CHESS1 = [["WB"[(w+h%2)%2] for w in range(8)] for h in range(8)]
# 체스판2
CHESS2 = [["BW"[(w+h%2)%2] for w in range(8)] for h in range(8)]

# 8 -> 0
# 9 -> 0, 1
# 10 -> 0, 1, 2
ret = 99999 #초기화용
for height_start in range(0, HEIGHT-7):
    for width_start in range(0, WIDTH-7):
        tmp1 = 0
        tmp2 = 0
        for h in range(8):
            for w in range(8):
                if CHESS1[h][w] != input_list[height_start+h][width_start+w] : tmp1 += 1
                if CHESS2[h][w] != input_list[height_start+h][width_start+w] : tmp2 += 1
        if tmp1 < ret : ret = tmp1
        if tmp2 < ret : ret = tmp2
sys.stdout.write(str(ret))
