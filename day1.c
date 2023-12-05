#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#define MAXLENGTH 1248

int value(int* total);

int main(){
	
	int i;
	int total = 0;
	int end = 0;
	int line = 1;

	while (1) {
		//printf("line num: %d", line);
		end = value(&total);
		line++;
		printf("total number: %d\n", total);
		if (end == 1) {
			break;
		}
	}
	printf("total number: %d", total);
	return 0;
}

int value(int* total) {
	char lastString[MAXLENGTH];
	char string[MAXLENGTH];
	int length = 0;
	char num[2];

	scanf(" %s", string);
	printf("%s\n", string);

	if (strcmp(lastString, string) == 0) {
		return 1;
	}
	strcpy(lastString, string);


	char fn;
	char ln;
	length = strlen(string);
	int i;
	//finds first num
	for (i = 0; i < length; i++) {
		if (isdigit(string[i])) {
			char fn = string[i];
			num[0] = fn;
			//printf("first num: %c\n", fn);
			break;
		}
	}

	for (i = length; i >= 0; i--) {
		if (isdigit(string[i])) {
			char ln = string[i];
			num[1] = ln;
			//printf("last num: %c\n", ln);
			break;
		}
	}
	//printf("total num: %s\n", num);
	int tnum = 0;
	char c;
	for (i = 0; i <= 9; i++) {
		c = i + '0';
		if (num[0] == c) {
			tnum += i * 10;
		}
	}
	for (i = 0; i <= 9; i++) {
		c = i + '0';
		if (num[1] == c) {
			tnum += i;
		}
	}

	printf("two num = %d\n", tnum);
	*total += tnum;
	return 0;
}