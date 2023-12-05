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

	scanf("%s", string);
	printf("%s\n", string);

	if (strcmp(lastString, string) == 0) {
		printf("endloop");
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
		if (string[i] == 'o' && string[i + 1] == 'n' && string[i + 2] == 'e') {
			char fn = 1 + '0';
			num[0] = fn;
			//printf("first num string: %c\n", fn);
			break;
		}

		if (string[i] == 't' && string[i + 1] == 'w' && string[i + 2] == 'o') {
			char fn = 2 + '0';
			num[0] = fn;
			//printf("first num string: %c\n", fn);
			break;
		}

		if (string[i] == 't' && string[i + 1] == 'h' && string[i + 2] == 'r' && string[i + 3] == 'e' && string[i + 4] == 'e') {
			char fn = 3 + '0';
			num[0] = fn;
			//printf("first num string: %c\n", fn);
			break;
		}

		if (string[i] == 'f' && string[i + 1] == 'o' && string[i + 2] == 'u' && string[i + 3] == 'r') {
			char fn = 4 + '0';
			num[0] = fn;
			//printf("first num string: %c\n", fn);
			break;
		}

		if (string[i] == 'f' && string[i + 1] == 'i' && string[i + 2] == 'v' && string[i + 3] == 'e') {
			char fn = 5 + '0';
			num[0] = fn;
			//printf("first num string: %c\n", fn);
			break;
		}

		if (string[i] == 's' && string[i + 1] == 'i' && string[i + 2] == 'x') {
			char fn = 6 + '0';
			num[0] = fn;
			//printf("first num string: %c\n", fn);
			break;
		}

		if (string[i] == 's' && string[i + 1] == 'e' && string[i + 2] == 'v' && string[i + 3] == 'e' && string[i + 4] == 'n') {
			char fn = 7 + '0';
			num[0] = fn;
			//printf("first num string: %c\n", fn);
			break;
		}

		if (string[i] == 'e' && string[i + 1] == 'i' && string[i + 2] == 'g' && string[i + 3] == 'h' && string[i + 4] == 't') {
			char fn = 8 + '0';
			num[0] = fn;
			//printf("first num string: %c\n", fn);
			break;
		}

		if (string[i] == 'n' && string[i + 1] == 'i' && string[i + 2] == 'n' && string[i + 3] == 'e') {
			char fn = 9 + '0';
			num[0] = fn;
			//printf("first num string: %c\n", fn);
			break;
		}

	}
	
	//finds last num
	for (i = length; i >= 0; i--) {
		if (isdigit(string[i])) {
			char ln = string[i];
			num[1] = ln;
			//printf("last num: %c\n", ln);
			break;
		}
		
		if (string[i] == 'e' && string[i - 1] == 'n' && string[i - 2] == 'o') {
			char ln = 1 + '0';
			num[1] = ln;
			//printf("first num string: %c\n", ln);
			break;
		}
		
		else if (string[i] == 'o' && string[i - 1] == 'w' && string[i - 2] == 't') {
			char ln = 2 + '0';
			num[1] = ln;
			//printf("first num string: %c\n", ln);
			break;
		}
		
		else if (string[i] == 'e' && string[i - 1] == 'e' && string[i - 2] == 'r' && string[i - 3] == 'h' && string[i - 4] == 't') {
			char ln = 3 + '0';
			num[1] = ln;
			//printf("first num string: %c\n", ln);
			break;
		}
		
		else if (string[i] == 'r' && string[i - 1] == 'u' && string[i - 2] == 'o' && string[i - 3] == 'f') {
			char ln = 4 + '0';
			num[1] = ln;
			//printf("first num string: %c\n", ln);
			break;
		}
		
		else if (string[i] == 'e' && string[i - 1] == 'v' && string[i - 2] == 'i' && string[i - 3] == 'f') {
			char ln = 5 + '0';
			num[1] = ln;
			//printf("first num string: %c\n", ln);
			break;
		}
		
		else if (string[i] == 'x' && string[i - 1] == 'i' && string[i - 2] == 's') {
			char ln = 6 + '0';
			num[1] = ln;
			//printf("first num string: %c\n", ln);
			break;
		}
		
		else if (string[i] == 'n' && string[i - 1] == 'e' && string[i - 2] == 'v' && string[i - 3] == 'e' && string[i - 4] == 's') {
			char ln = 7 + '0';
			num[1] = ln;
			//printf("first num string: %c\n", ln);
			break;
		}
		
		else if (string[i] == 't' && string[i - 1] == 'h' && string[i - 2] == 'g' && string[i - 3] == 'i' && string[i - 4] == 'e') {
			char ln = 8 + '0';
			num[1] = ln;
			//printf("first num string: %c\n", ln);
			break;
		}
		
		else if (string[i - 3] == 'n' && string[i - 2] == 'i' && string[i - 1] == 'n' && string[i] == 'e') {
			char ln = 9 + '0';
			num[1] = ln;
			//printf("first num string: %c\n", ln);
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