#pragma warning (disable : 4996)
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int n, m;
int friend[51][51] = { 0 };
int visited[51] = { 0 };
int total[51] = { 0 };

typedef struct Node {
	int level;
	int num;
	struct Node* nextnode;
} Node;
typedef struct Queue {
	Node* front;
	Node* rear;
} Queue;

Queue* createQ(Queue* Q) {
	Q->front = NULL;
	Q->rear = NULL;
	return Q;
}
Node* createN(int level, int num) {
	Node* node = (Node*)malloc(sizeof(Node));
	node->level = level;
	node->num = num;
	node->nextnode = NULL;
	return node;
}
void enqueue(Queue* Q, Node* N) {
	if (Q->front == NULL) Q->front = N;
	else Q->rear->nextnode = N;
	Q->rear = N;
}
int dequeue(Queue* Q) {
	Node* tmp = Q->front;
	int data = Q->front->num;
	if (Q->front->nextnode == NULL) Q->rear = NULL;
	Q->front = Q->front->nextnode;
	free(tmp);
	return data;
}
bool isEmpty(Queue* Q) {
	return Q->rear == NULL;
}

//각 사람마다 케빈 베이컨 수를 구하는 함수
void bfs(int num) {
	int level = 0;
	for (int i = 1; i <= n; i++) { //방문여부 초기화
		visited[i] = 0;
	}
	Queue* Q = (Queue*)malloc(sizeof(Queue));
	Q = createQ(Q);
	Node* nd = createN(level, num);
	enqueue(Q, nd);
	visited[num] = 1;

	while (!isEmpty(Q)) {
		level = Q->front->level; 
		int d = dequeue(Q);
		for (int i = 1; i <= n; i++) {
			if (friend[d][i] == 1 && visited[i] == 0) {  //친구 관계이고 아직 방문하지 않은 경우
				visited[i] = 1;
				Node* new = createN(level + 1, i);
				enqueue(Q, new);
				total[num] += level + 1;   //케빈 베이컨 수 저장
			}
		}
	}

}

int main() {
	int t1, t2, final = 0;
	scanf("%d %d", &n, &m);
	for (int i = 0; i < m; i++) {
		scanf("%d %d", &t1, &t2);
		friend[t1][t2] = friend[t2][t1] = 1;
		friend[t1][t1] += 1;
		friend[t2][t2] += 1;
		if (t1 > final) final = t1;
		if (t2 > final) final = t2; 
	}
	for (int i = 1; i <= final; i++) {
		if(friend[i][i]!=0) bfs(i);
	}
	int min = 5005;
	int p = 1;
	for (int i = 1; i <= final; i++) {
		if (friend[i][i] == 0) continue;
		if (total[i] < min) {
			min = total[i];
			p = i;
		}
	}
	printf("%d", p);

	return 0;
}
