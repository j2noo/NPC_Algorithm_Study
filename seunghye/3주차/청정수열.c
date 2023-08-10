#pragma warning (disable : 4996)
#include <stdio.h>

int main() {
	int n, num = 1;
	scanf("%d", &n);

	for (int i = 2; i <= n; i++) {
		num *= i;
	}
	printf("%d", num);

	return 0;
}
