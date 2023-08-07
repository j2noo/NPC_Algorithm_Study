from sys import stdin


N, W = map(int, stdin.readline().split())
incidence_li = [[] for _ in range(500010)]
cnt_leaf_node = 0

for _ in range(N - 1):
    U, V = map(int, stdin.readline().split())
    incidence_li[U].append(V)
    incidence_li[V].append(U)

for i in range(2, N + 1):
    if len(incidence_li[i]) == 1:
        cnt_leaf_node += 1

print(W / cnt_leaf_node)
