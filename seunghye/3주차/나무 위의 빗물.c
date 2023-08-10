#pragma warning (disable : 4996)
#include <stdio.h>
#include <stdlib.h>

int main() {
	int n, u, v, cnt = 0;
	long long w;
	int *node;

	scanf("%d %lld", &n, &w);
	node = (int*)malloc((n+1) * sizeof(int));
	for (int i = 0; i < n+1; i++) {
		node[i] = 0;
	}
	
	for (int i = 0; i < n-1; i++) {
		scanf("%d %d", &u, &v);
		node[u] += 1;
		node[v] += 1;
	}
	for (int i = 2; i <= n; i++) {
		if (node[i] == 1) cnt++;
	}
	printf("%lf", w / (double)cnt);

	return 0;
}
