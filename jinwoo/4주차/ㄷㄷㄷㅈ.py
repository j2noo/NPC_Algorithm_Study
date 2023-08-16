import math
import itertools

N = int(input())

incidence_li = list([] for _ in range(N + 1))

cntD, cntG = 0, 0

for _ in range(N - 1):
    u, v = map(int, input().split())
    # v가 부모
    if u > v:
        incidence_li[v].append(u)
    else:
        incidence_li[u].append(v)


# for i in range(N + 1):
#     print(incidence_li[i])


# n번노드에서 ㄷ,ㅈ의 개수 1
def solve1(n):
    cnt = 0
    for node_depth_2 in incidence_li[n]:
        for node_depth_3 in incidence_li[node_depth_2]:
            for node_depth_4 in incidence_li[node_depth_3]:
                cnt += 1
    return cnt


# n번노드에서 ㄷ,ㅈ의 개수 2
def solve2(n):
    cnt = 0
    for node_depth_2 in incidence_li[n]:
        cnt_depth2 = len(incidence_li[node_depth_2])
        cnt += math.comb(cnt_depth2, 2)
    return cnt


# n번노드에서 ㄷ,ㅈ의 개수 3
def solve3(n):
    cnt = 0
    select_two = itertools.combinations(incidence_li[n], 2)
    for li in select_two:
        # print(list(li))
        cnt += len(incidence_li[list(li)[0]])
        cnt += len(incidence_li[list(li)[1]])
    return cnt


# n번노드에서 ㄷ,ㅈ의 개수 4
def solve4(n):
    cnt = 0
    cnt_depth1 = len(incidence_li[n])
    cnt += math.comb(cnt_depth1, 3)
    return cnt


for i in range(1, N + 1):
    # print("solve1 : ", solve1(i))
    # print("solve2 : ", solve2(i))
    # print("solve3 : ", solve3(i))
    # print("solve4 : ", solve4(i))
    cntD += solve1(i)
    cntG += solve2(i)

    cntD += solve3(i)

    cntG += solve4(i)

# print(f"ㄷ : {cntD} ㅈ : {cntG}")
if cntD > cntG * 3:
    print("D")
elif cntD < cntG * 3:
    print("G")
else:
    print("DUDUDUNGA")
