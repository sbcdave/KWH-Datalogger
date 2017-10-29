#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <errno.h>
#include <getopt.h>

int main(void) {
	char *line;
	char *line2;
	char test[30];
	test[0]='\r';
	test[1]='\n';
	line = "te";
	line2 = line;
	line++;
	printf(line2);
	printf(line);
	line=test;
	printf(line);
	return 0;
}
