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
	if (num[0] == '1') {
		tnum += 10;
	}
	else if (num[0] == '2') {
		tnum += 20;
	}
	else if (num[0] == '3') {
		tnum += 30;
	}
	else if (num[0] == '4') {
		tnum += 40;
	}
	else if (num[0] == '5') {
		tnum += 50;
	}
	else if (num[0] == '6') {
		tnum += 60;
	}
	else if (num[0] =='7') {
		tnum += 70;
	}
	else if (num[0] == '8') {
		tnum += 80;
	}
	else if (num[0] == '9') {
		tnum += 90;
	}

	if (num[1] == '1') {
		tnum += 1;
	}
	else if (num[1] == '2') {
		tnum += 2;
	}
	else if (num[1] == '3') {
		tnum += 3;
	}
	else if (num[1] == '4') {
		tnum += 4;
	}
	else if (num[1] == '5') {
		tnum += 5;
	}
	else if (num[1] == '6') {
		tnum += 6;
	}
	else if (num[1] == '7') {
		tnum += 7;
	}
	else if (num[1] == '8') {
		tnum += 8;
	}
	else if (num[1] == '9') {
		tnum += 9;
	}
	printf("two num = %d\n", tnum);
	*total += tnum;
	return 0;
}