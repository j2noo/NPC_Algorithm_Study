#pragma warning (disable : 4996)
#include <stdio.h>
#include <stdlib.h>

int N, L, R;
int a[50][50], visited[50][50];
int day = 0, cnt, population;

int diff(int i, int j) {
	if (i > j) return i - j;
	else return j - i;
}
void find(int r, int c) {
	visited[r][c] = 1;
	population += a[r][c];

	if (r - 1 >= 0 && visited[r - 1][c] == 0 && L <= diff(a[r][c], a[r - 1][c]) && diff(a[r][c], a[r - 1][c]) <= R) {
		cnt += 1;
		find(r - 1, c);
	}
	if (r + 1 < N && visited[r + 1][c] == 0 && L <= diff(a[r][c], a[r + 1][c]) && diff(a[r][c], a[r + 1][c]) <= R) {
		cnt += 1;
		find(r + 1, c);
	}
	if (c - 1 >= 0 && visited[r][c - 1] == 0 && L <= diff(a[r][c], a[r][c - 1]) && diff(a[r][c], a[r][c - 1]) <= R) {
		cnt += 1;
		find(r, c - 1);
	}
	if (c + 1 < N && visited[r][c + 1] == 0 && L <= diff(a[r][c], a[r][c + 1]) && diff(a[r][c], a[r][c + 1]) <= R) {
		cnt += 1;
		find(r, c + 1);
	}
}
void change(int p) {
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (visited[i][j] == 1) {
				a[i][j] = p;
				visited[i][j] = 2;
			}
		}
	}
}

int main() {
	scanf("%d %d %d", &N, &L, &R);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			scanf("%d", &a[i][j]);
		}
	}
	if (N != 1) {
		while (1) {
			int f = 0;
			for (int i = 0; i < N; i++) { //방문 여부 초기화
				for (int j = 0; j < N; j++) {
					visited[i][j] = 0;
				}
			}
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					cnt = 1;
					population = 0;
					if (visited[i][j] == 0) {
						find(i, j);
						if (cnt > 1) {
							f = 1;
							change(population / cnt);
						}
						else if (cnt == 1) visited[i][j] = 0;
					}
					if (cnt == N * N) {
						f = 2;
						break;
					}
				}
				if (f == 2) break;
			}
			if (f == 1 || f==2) day += 1;
			if (f == 0) break;
		}
	}
	printf("%d", day);

	return 0;
}
