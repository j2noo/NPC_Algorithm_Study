#pragma warning (disable : 4996)
#include <stdio.h>

int max(int a, int b, int c) {
	int mx = a;
	if (mx < b) mx = b;
	if (mx < c) mx = c;
	return mx;
}

int main() {
	int n, amount[10000], dp[10000];

	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &amount[i]);
	}

	dp[0] = amount[0];
	if (n > 1) {
		dp[1] = amount[0] + amount[1];
		if (n > 2) {
			dp[2] = max(amount[2] + amount[1], amount[2] + amount[0], amount[0] + amount[1]);
			for (int i = 3; i < n; i++) {
				dp[i] = max(amount[i] + amount[i - 1] + dp[i - 3], amount[i] + dp[i - 2], dp[i - 1]);
			}
		}
	}
	printf("%d", dp[n-1]);


	return 0;
}
