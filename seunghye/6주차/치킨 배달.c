#pragma warning (disable : 4996)
#include <stdio.h>
#include <stdlib.h>

int n, m, ch_cnt;
int city[51][51], choose_num[13], min_num[13], min=9999999;

typedef struct node {
	int rn, cn;
	long long house;
	int choose;
} node;
typedef struct ch {
	node* nodes;
	int cnt;
} ch;

int d(int r1, int c1, int r2, int c2) {
	return abs(r1 - r2) + abs(c1 - c2);
}

void choose_m(ch* ck, int start, ch* hs) {  //m개의 치킨 집을 선택하는 함수
	int total;
	for (int i = start; i < ck->cnt; i++) {
		if (ck->nodes[i].choose == 1) continue;
		choose_num[ch_cnt] = i;
		ch_cnt++;
		ck->nodes[i].choose = 1;
		if (ch_cnt == m) {     //m개를 선택한 경우
			total = calculate(hs, ck);
			if (total < min) {   //도시의 치킨 거리 값의 최소를 찾은 경우, 값과 해당 치킨 집 정보 저장
				min = total;
				for (int j = 0; j < m; j++) {
					min_num[j] = choose_num[j];
				}
			}
		}
		else choose_m(ck, i + 1, hs);
		ch_cnt--;
		ck->nodes[i].choose = 0;
	}
}
int calculate(ch* hs, ch* ck) {   //선택된 m개의 치킨 집에 대한 도시의 치킨 거리 값 구하는 함수
	int total = 0, dis = 0, mn;
	for (int i = 0; i < hs->cnt; i++) {
		mn = d(hs->nodes[i].rn, hs->nodes[i].cn, ck->nodes[choose_num[0]].rn, ck->nodes[choose_num[0]].cn);
		for (int j = 1; j < m; j++) {
			dis = d(hs->nodes[i].rn, hs->nodes[i].cn, ck->nodes[choose_num[j]].rn, ck->nodes[choose_num[j]].cn);
			if (dis < mn) mn = dis;
		}
		total += mn;
	}
	return total;
}

int main() {
	scanf("%d %d", &n, &m);

	ch* ck = (ch*)malloc(sizeof(ch));
	ck->nodes = (node*)malloc(sizeof(node) * 13);
	ck->cnt = 0;
	ch* hs = (ch*)malloc(sizeof(ch));
	hs->nodes = (node*)malloc(sizeof(node) * 2 * n);
	hs->cnt = 0;

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			scanf("%d", &city[i][j]);
			if (city[i][j] == 1) { //집 위치 저장
				hs->nodes[hs->cnt].rn = i;
				hs->nodes[hs->cnt].cn = j;
				hs->cnt++;
			} 
			else if (city[i][j] == 2) {  //치킨 집 위치 저장
				ck->nodes[ck->cnt].rn = i;
				ck->nodes[ck->cnt].cn = j;
				ck->nodes[ck->cnt].house = ck->nodes[ck->cnt].choose = 0;
				ck->cnt++;
			}
		}
	}
	choose_m(ck, 0, hs);
	printf("%d", min);

	return 0;
}
