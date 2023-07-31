//1026번, 보물
#pragma warning (disable : 4996)
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

int compare(const int* a, const int* b) {
	return (*a - *b);
}

int main() {
	int n, cnt, sum = 0;
	int arr1[50], arr2[50], idx[50];

	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &arr1[i]);
	}
	for (int i = 0; i < n; i++) {
		scanf("%d", &arr2[i]);
	}
	qsort(arr1, n, sizeof(int), compare);  //오름차순 정렬

	//arr2의 순위 구하기
	for (int i = 0; i < n; i++) {
		cnt = 0;
		for (int j = 0; j < n; j++) {
			if (arr2[i] < arr2[j]) cnt++;
			else if (arr2[i] == arr2[j]) {
				if (i > j) cnt++;
			}
		}
		idx[i] = cnt;
	}

	for (int i = 0; i < n; i++) {
		sum += arr2[i] * arr1[idx[i]];
	}
	printf("%d", sum);
	
	return 0;
}
