//1018번, 체스판 다시 칠하기
#pragma warning (disable : 4996)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	int n, m, tmp, min = 2501;
	char ch[50][51];

	scanf("%d %d", &n, &m);
	for (int i = 0; i < n; i++) {
		scanf("%s", ch[i]);
	}
	
	//시작 지점이 될 수 있는 위치 모두 고려
	for (int nn = 0; nn < n - 7; nn++) {
		for (int mm = 0; mm < m - 7; mm++) {
			tmp = 0;

			//시작 지점부터 8칸, 시작 지점이 'W'로 시작한다고 가정
			for (int nnn = nn; nnn < nn + 8; nnn++) {
				for (int mmm = mm; mmm < mm + 8; mmm++) {
					if ((nnn - nn + mmm - mm) % 2 == 0) {
						if (ch[nnn][mmm] != 'W') {
							tmp++;
						}
					}
					else {
						if (ch[nnn][mmm] != 'B') {
							tmp++;
						}
					}
				}
			}
				
			//카운트가 32보다 큰 경우 -> 시작 지점이 'B'일 때가 더 적음
			if (tmp > 32) tmp = 64 - tmp;
			if (tmp < min) min = tmp;
		}
	}
	printf("%d", min);

	return 0;
}
