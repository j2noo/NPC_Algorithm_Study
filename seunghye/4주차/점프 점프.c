#pragma warning (disable : 4996)
#include <stdio.h>

int main() {
	int n, arr[1000] = { 0 }, jump[1000];
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
		jump[i] = 10000;
	}
	if (arr[0] == 0 && n == 1) printf("0");
	else if (arr[0] == 0 && n > 1) printf("-1");
	else {
		jump[0] = 0;
		jump[1] = 1;
		for (int i = 2; i < n; i++) {
			for (int j = 0; j < i; j++) {
				if (arr[j] >= i - j) {
					if (jump[j] + 1 < jump[i]) {
						jump[i] = jump[j] + 1;
					}
				}
			}
		}
		if (jump[n - 1] == 10000) printf("-1");
		else printf("%d", jump[n - 1]);
	}
	
	return 0;
}
