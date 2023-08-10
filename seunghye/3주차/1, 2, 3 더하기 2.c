#pragma warning (disable : 4996)
#include <stdio.h>

int cnt = 0;
int find(int *result, int n, int k,int idx);

int main() {
	int n, k;
	int result[20]={0}, re;
	scanf("%d %d", &n, &k);
	
	re = find(&result, n, k, 0);
	if (re == 0) printf("-1");

	return 0;
}
int find(int *result, int n, int k, int idx) {
	int tmp, sum = 0;
	for (int i = 0; i < idx; i++) {
		sum += *(result+i);
	}

	if (sum == n) {
		cnt = cnt + 1;
		if (cnt == k) {
			for (int i = 0; i < idx - 1; i++) {
				printf("%d", *(result+i));
				printf("+");
			}
			printf("%d", *(result+idx-1));
			return 1;
		}
		return 0;
	}
	else if (sum > n) return 0;

	for (int i = 1; i <= 3; i++) {
		*(result+idx) = i;
		idx += 1;
		tmp = find(result, n, k, idx);
		if (tmp == 1) return 1;
		idx -= 1;
	}
	return 0;
}
