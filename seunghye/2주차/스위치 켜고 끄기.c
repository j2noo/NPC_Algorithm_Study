//2주차 - 1244번, 스위치 켜고 끄기
#pragma warning (disable : 4996)
#include <stdio.h>

int main() {
	int sw_n, state[101], st_num, f, num, tmp;

	scanf("%d", &sw_n);
	for (int i = 1; i <= sw_n; i++) {
		scanf("%d", &state[i]);
	}

	scanf("%d", &st_num);
	for (int i = 0; i < st_num; i++) {
		scanf("%d %d", &f, &num);
		if (f == 1) {
			tmp = num;
			//남학생, 받은 수의 배수에서 스위치 상태를 바꿈
			while (tmp <= sw_n) {
				state[tmp] = (state[tmp] + 1) % 2;
				tmp = tmp + num;
			}
		}
		else {
			//여학생, 받은 수에서 대칭이 끝나기 직전 구간까지
			state[num] = (state[num] + 1) % 2;
			tmp = 1;
			while (num + tmp <= sw_n && num - tmp > 0) {
				if (state[num + tmp] == state[num - tmp]) {
					state[num + tmp] = (state[num + tmp] + 1) % 2;
					state[num - tmp] = (state[num - tmp] + 1) % 2;
					tmp += 1;
				}
				else break;
			}
		}
	}

	for (int i = 1; i <= sw_n; i++) {
		printf("%d ", state[i]);
		if (i % 20 == 0) printf("\n");
	}

	return 0;
}
