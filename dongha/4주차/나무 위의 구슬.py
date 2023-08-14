import sys
def input() : return sys.stdin.readline().rstrip()
print = sys.stdout.write

#sys.stdin = open("input.txt", 'r')

NUM = int(input())
tree = [[0,0]]
for i in range(1, NUM+1):
    tree.append(list(map(int, input().split())))
K = int(input())

# 트리 규칙 :
# 항상 왼쪽이 오른쪽보다 크거나 같다.

# k가 0이상 정수일 때
# 지금 들고 있는 구슬이 2k+1번째 구슬이며(초기 K),
# == 트리에 남은 구슬이 2k개라면 ********
# 왼쪽은 k개, 오른쪽도 k게
# (무조건 왼쪽으로 간다.) - 인덱스 0
# ( 2k // 2 ) 개를 빼면 된다. 
# 
# 지금 들고 있는 구슬이 2k번째 구슬이며(초기 K),
# == 트리에 남은 구슬이 2k-1개라면 ********
# 왼쪽은 k개, 오른쪽은 k-1개
# (무조건 오른쪽으로 간다.) - 인덱스 1
# ( (2k-1)//2 +1 ) 개를 빼면 된다.
# 
# 예외상황1 : 
# 자식노드가 1개라면 갯수 감소 없이 그대로 간다.
# 예외상황2 :
# 자식노드가 없다면 거기 종점번호가 문제 답이다.

idx_now = 1
k = K-1 
#현재 트리에 남아있는 구슬의 갯수가 기준이라 -1해줌
while tree[idx_now] != [-1, -1] :
    if -1 not in tree[idx_now]:
        if k %2 == 0:
            k //= 2
            idx_now = tree[idx_now][0]
        else:
            k -= (k//2 + 1)
            idx_now = tree[idx_now][1]
    else:
        # 둘 중 -1 아닌 인덱스가 다음 인덱스.
        # 둘다 -1인 경우는 위 while문 조건으로 걸림
        idx_now = max(tree[idx_now][0],tree[idx_now][1])
print(str(idx_now))