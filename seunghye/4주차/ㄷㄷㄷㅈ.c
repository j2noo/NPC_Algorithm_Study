#pragma warning (disable : 4996)
#include <stdio.h>
#include <stdlib.h>

typedef struct {  //ㄷ의 개수를 구하기 위해 연결된 정점의 관계를 저장
	int n1;
	int n2;
} link;

int main() {
	link* e = NULL;
	int n, u, v;
	int tree[300001] = { 0, };
	int dcnt = 0, zcnt = 0, tmp;

	scanf("%d", &n);
	e = (link*)malloc(sizeof(link) * n);
	for (int i = 0; i < n - 1; i++) {
		scanf("%d %d", &u, &v);
		tree[u] += 1;
		tree[v] += 1;
		e[i].n1 = u;   //입력받은 순서대로 구조체 배열에 저장
		e[i].n2 = v;
	}

  //ㅈ 모양의 개수 : 해당 정점에 연결된 정점들의 개수로
	for (int i = 1; i <= n; i++) {  
		tmp = tree[i];
		if (tree[i] >= 3) zcnt += (tmp * (tmp - 1) * (tmp - 2)) / 6;
	}

  //ㄷ 모양의 개수 : (해당 정점에 연결된 정점의 개수 - 1), (연결된 정점에 연결된 정점의 개수 - 1) -> 서로 연결되어 카운트 된 1 제거
	for (int i = 0; i < n-1; i++) {
		u = e[i].n1;
		v = e[i].n2;
		dcnt += (tree[u] - 1) * (tree[v] - 1);
	}

	if (dcnt > zcnt * 3) printf("D");
	else if (dcnt < zcnt * 3) printf("G");
	else printf("DUDUDUNGA");

	return 0;
}
