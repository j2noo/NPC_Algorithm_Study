//2주차 - 2579번, 계단 오르기
#pragma warning (disable : 4996)
#include <stdio.h>

#define max(a, b) (a<b)?b:a

int main() {
	//n번 계단까지 가는 최댓값 저장 -> 필요할 때 사용
	int n, st[300], max_st[300] = { 0 }, sum = 0, tmp;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &st[i]);
	}

	max_st[0] = st[0];
	max_st[1] = max(st[0] + st[1], st[1]);
	max_st[2] = max(st[0] + st[2], st[1] + st[2]);
	//i-1 계단 (i + i-1 + max(i-3)) vs i-2 계단 (i + max(i-2))
	for (int i = 3; i < n; i++) {
		max_st[i] = max(st[i] + st[i - 1] + max_st[i - 3], st[i] + max_st[i - 2]);
	}
	printf("%d", max_st[n - 1]);

	return 0;
}
