import math
import itertools
import sys

sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())

incidence_li = list([] for _ in range(N + 1))
parent_li = [-1] * (N + 1)
child_cnt = [0] * (N + 1)
edge_li = []

cntD, cntG = 0, 0

for _ in range(N - 1):
    u, v = map(int, sys.stdin.readline().split())
    incidence_li[v].append(u)
    incidence_li[u].append(v)
    edge_li.append([u, v])


def solveG(n):
    cnt_children = len(incidence_li[n])
    return math.comb(cnt_children, 3)


# ㅈ
for i in range(1, N + 1):
    cntG += solveG(i)

# ㄷ
for edge in edge_li:
    u, v = edge
    cntD += (len(incidence_li[u]) - 1) * (len(incidence_li[v]) - 1)

# print(f"ㄷ : {cntD} ㅈ : {cntG}")
if cntD > cntG * 3:
    print("D")
elif cntD < cntG * 3:
    print("G")
else:
    print("DUDUDUNGA")
