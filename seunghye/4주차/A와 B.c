#pragma warning (disable : 4996)
#include <stdio.h>
#include <string.h>

void swap(char* a, char* b) {
	char tmp = *a;
	*a = *b;
	*b = tmp;
}

int main() {
	char s[1000], t[1001];
	int slen, tlen;

	scanf("%s", s);
	scanf("%s", t);
	slen = strlen(s);
	tlen = strlen(t);

	while (slen <= tlen) {
		if (strcmp(s,t)==0) {
            		printf("1"); 
            		break;	
        	}
		else {
			if (t[tlen - 1] == 'A') {
				tlen -= 1;
                		t[tlen]='\0';
			}
			else {
				tlen -= 1;
				t[tlen] = '\0';
				for (int i = 0; i < tlen/2; i++) {
					swap(&t[i], &t[tlen - i - 1]);
				}
			}
		}
	}
    	if(slen!=tlen) printf("0");

	return 0;
}
