#pragma warning (disable : 4996)
#include <stdio.h>

int main() {
	int t, n, tmp1 = 0, tmp2 = 0, pass, grade;
	int in_score[100000]={0};

	scanf("%d", &t);
	
	//서류 순위대로 면접 순위 저장
	for (int test = 0; test < t; test++) {
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			scanf("%d %d", &tmp1, &tmp2);
			in_score[tmp1 - 1] = tmp2;
		}

		pass = 1; //서류 1위는 무조건 통과
		grade = in_score[0]; 

		for (int i = 1; i < n; i++) {
			if (in_score[i] < grade) {
				pass++;
				grade = in_score[i];
			}
		}
		printf("%d\n", pass);
	}

	return 0;
}
