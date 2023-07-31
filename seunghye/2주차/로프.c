//2주차 - 2217번, 로프 
#pragma warning (disable : 4996)
#include <stdio.h>

int compare(const int* n, const int* m) {
	return (*n - *m);
}

int main() {
	//로프 중량 * k(개) = w(총 중량)
	int n, input[100000], tmp, max = 0;
	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		scanf("%d", &input[i]);
	}

	//오름차순 정렬 : 시간 초과 -> 퀵 정렬
	/*for (int i = 0; i < n - 1; i++) {
		for (int j = i; j < n; j++) {
			if (input[i] > input[j]) {
				tmp = input[i];
				input[i] = input[j];
				input[j] = tmp;
			}
		}
	}*/
	qsort(input, n, sizeof(int), compare);

	//최대 중량 찾기
	for (int i = 0; i < n; i++) {
		tmp = input[i] * (n - i);
		if (tmp > max) max = tmp;
	}
	printf("%d", max);

	return 0;
}
