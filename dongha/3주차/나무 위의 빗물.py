# 답 : W / 최말단 노드 개수
# 최말단 노드 특징 : 1 이 아니며, 자신으로부터 이어진 노드가 단 하나만 존재
import sys
#sys.stdin = open('input.txt', 'r')

N, W = map(int, sys.stdin.readline().split())
actually_not_a_graph = [2] * (N+1)
actually_not_a_graph[0] = 0 # 더미노드 제거
actually_not_a_graph[1] = 0 # 1이 최말단 노드가 될 수는 없다.
itersystem = map(int, sys.stdin.read().split())
for i in itersystem:
    actually_not_a_graph[i] >>= 1 # 2는 1로, 1은 0으로, 0은 0으로
sys.stdout.write(str(W/sum(actually_not_a_graph)))
