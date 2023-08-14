import sys
def input() : return sys.stdin.readline().rstrip()
print = sys.stdout.write

#sys.stdin = open("input.txt", 'r')

N = int(input())
lines_list = []
legs_list = [0] * (N+1)

for _ in range(N-1):
    v1, v2 = map(int, input().split())
    legs_list[v1] += 1
    legs_list[v2] += 1
    lines_list.append((v1, v2))

num_D = 0
num_G = 0

# 'ㄷ'의 갯수
for i in lines_list:
    v1, v2 = i
    num_D += ((legs_list[v1]-1) * ((legs_list[v2]-1)))

# 'ㅈ'의 갯수
for i in legs_list:
    if i >= 3:
        num_G += (i*(i-1)*(i-2))//6

if num_D == 3 * num_G:
    print("DUDUDUNGA")
elif num_D > 3 * num_G:
    print("D")
else:
    print("G")
print("\n")