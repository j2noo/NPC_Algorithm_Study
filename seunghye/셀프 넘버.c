//4673번, 셀프 넘버
#pragma warning (disable : 4996)
#include <stdio.h>

int main() {
	int check[10000] = { 0 };
	int tmp1 = 1, tmp2 = 0;

	for (int i = 1; i < 10000; i++) {
		tmp1 = i;
		tmp2 = tmp1;
		while (tmp1 > 0) {
			tmp2 += tmp1 % 10;
			tmp1 /= 10;
		}
		if (tmp2 <= 10000) check[tmp2 - 1] = 1;
	}
	
	for (int i = 0; i < 10000; i++) {
		if (check[i] == 0) printf("%d\n", i + 1);
	}


	return 0;
}
