//11726번, 2xn 타일링
#pragma warning (disable : 4996)
#include <stdio.h>

int main() {
	int n;
	scanf("%d", &n);

	int one = 1, two = 2, cnt = 0;

	if (n == 1) printf("1");
	else if (n == 2) printf("2");
	else {
		//피보나치 수열 규칙 적용해서 계산
		//10007을 더하는 과정에서 나눠줘야 오버플로 발생을 막을 수 있음
		for (int i = 3; i <= n; i++) {
			cnt = (one + two) % 10007;
			one = two;
			two = cnt;
		}
		printf("%d", cnt);
	}

	return 0;
}
