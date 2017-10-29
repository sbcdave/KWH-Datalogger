#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <errno.h>
#include <getopt.h>

char * line_builder(FILE *fp) {
   int c;
   char *ret; 
   char str[4096];
   int n = 0;

   do {
	c = fgetc(fp);
	if(c == '\n' || c == '\r' || c == '\0' || c == '>') {
		printf("END\n\n");
		break ;
	}
	str[n] = (char)c;
	n++;
   } while(1);
   ret=str;
   fclose(fp);
   return ret;
}

int main(void) {
	FILE *fp = stdin;
	char *line;
//	fp = fopen("/dev/ttyAMA0", "r");
	line = line_builder(fp);
	printf(line);
	return 0;
}
