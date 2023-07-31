//10988번, 펠린드롬인지 확인하기
#pragma warning (disable : 4996)
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

int main() {
	char str1[101], str2[101] = { 0 };
	int len;

	scanf("%s", str1);
	len = strlen(str1);

	//단어를 뒤집어서 저장
	for (int i = 0; i < len; i++) {
		str2[i] = str1[len - i - 1];
	}
	str2[len] = '\0';
	
	//원래 단어랑 뒤집은 단어가 일치하는지 비교
	if (strcmp(str1, str2) == 0) printf("1");
	else printf("0");

	return 0;
}
