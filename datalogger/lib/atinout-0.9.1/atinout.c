/*
 * atinout
 *
 * This program takes AT commands as input, sends them to the modem and outputs
 * the responses.
 *
 * Copyright (C) 2013 Håkon Løvdal <hlovdal@users.sourceforge.net>
 *
 * ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 *
 *     This program is free software: you can redistribute it and/or modify
 *     it under the terms of the GNU General Public License as published by
 *     the Free Software Foundation, either version 3 of the License, or
 *     (at your option) any later version.
 *
 *     This program is distributed in the hope that it will be useful,
 *     but WITHOUT ANY WARRANTY; without even the implied warranty of
 *     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *     GNU General Public License for more details.
 *
 *     You should have received a copy of the GNU General Public License
 *     along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 *
 * Modified by: Dave Goldsmith - sbcdave
 * Date:        24 Oct 2017
 *
 * Reason:      is_final_result function wasn't catching responses that
 *              I needed to hanlde for the SIM800L. e.g. AT+CIPSHUT
 *              was responding with SHUT OK, and the case statement didn't
 *              cover that. Also added cases for a returned IP address,
 *              CLOSE OK, and the @888 response from the KWH server 
 *              upon successful transmision. I was unable to resolve the >
 *              response that AT+CIPSEND sends back because the SIM800L
 *              doesn't include a \n at the end of that response, which is
 *              a requirement for fgets(). I'm hanlding the CIPSEND 
 *              by echoing into the device instead.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <errno.h>
#include <getopt.h>

#define MAX_LINE_LENGTH (4 * 1024)
static char buf[MAX_LINE_LENGTH];
static int DEBUG=1;

static struct option long_options[] = {
	{"help", no_argument, NULL, 'h'},
	{"version", no_argument, NULL, 'V'},
	{"usage", no_argument, NULL, 0},
	{NULL, 0, NULL, 0}
};
static const char *short_options = "hV";

static void usage(const char * const argv0)
{
	printf("Usage: %s <input_file> <modem_device> <output_file>\n", argv0);
	printf("\n");
	printf("\t<input_file> is a file with AT commands to be executed. Value '-' means standard input.\n");
	printf("\t<input_file> is the device file for the modem (e.g. /dev/ttyACM0, /dev/ttyS0, etc).\n");
	printf("\t<output_file> is a file the responses to the AT commands are saved. Value '-' means standard output.\n");
	printf("\n");
	printf("In addition the program supports the following options:\n");
	printf("\n");
	printf("\t-h|--help\n");
	printf("\t-V|--version\n");
	printf("\t--usage\n");
	printf("\n");
}

static void help(const char * const argv0)
{
	printf("This program takes AT commands as input, sends them to the modem and outputs\n");
	printf("the responses.\n");
	printf("\n");
	printf("Example:\n");
	printf("\n");
	printf("$ echo 'AT+CPBS=\"ME\",\"ME\"; +CPBR=?' | %s - /dev/ttyACM0 -\n", argv0);
	printf("AT+CPBS=\"ME\",\"ME\"; +CPBR=?\n");
	printf("\n");
	printf("+CPBR: (1-7000),80,62\n");
	printf("\n");
	printf("OK\n");
	printf("$\n");

}

/* Replace '\n' with '\r', aka `tr '\012' '\015'` */
/*
static bool tr_lf_cr(const char *s)
{
	if(DEBUG){
		printf("tr_lf_cr\n");
	}
        char *p;
        p = strchr(s, '\n');
        if (p == NULL || p[1] != '\0') {
                return false;
        }
        *p = '\r';
        return true;
}
*/
/*
static void strip_cr(char *s)
{
	if(DEBUG){
		printf("strip_cr\n");
	}
	char *from, *to;
	from = to = s;
	// This seems like it could cause the program to go rogue
	// through memory looking for \0 or \r
	while (*from != '\0') {
		if (*from == '\r') {
			from++;
			continue;
		}
		*to++ = *from++;
	}
	*to = '\0';
}
*/
static bool is_final_result(const char * const response)
{
	if(DEBUG){
		printf("is_final_result\n");
		printf(response);
	}

	switch (response[0]) {
	case '+':
		return true;
	case 'B':
		if (strcmp(&response[1], "USY\r\n") == 0) {
			return true;
		}
		return false;

	case 'E':
		if (strcmp(&response[1], "RROR\r\n") == 0) {
			return true;
		}
		return false;
	case 'N':
		if (strcmp(&response[1], "O ANSWER\r\n") == 0) {
			return true;
		}
		if (strcmp(&response[1], "O CARRIER\r\n") == 0) {
			return true;
		}
		if (strcmp(&response[1], "O DIALTONE\r\n") == 0) {
			return true;
		}
		return false;
        case 'S':
                if (strcmp(&response[1], "HUT OK\r\n") == 0) {
                        return true;
                }
                return false;
        case 'C':
                if (strcmp(&response[1], "LOSE OK\r\n") == 0) {
                        return true;
                }
                return false;
        case '@':
                if (strcmp(&response[1], "888\n") == 0) {
                        return true;
                }
                return false;
        case '>':
                return true;
        case '1':
                return true;
        case '2':
                return true;
        case '3':
                return true;
        case '4':
                return true;
        case '5':
                return true;
        case '6':
                return true;
        case '7':
                return true;
        case '8':
                return true;
        case '9':
                return true;
	case 'O':
		return true;
	default:
		return false;
	}

}

char * line_builder(FILE *fp) {
   int c;
   char *ret; 
   char str[4096];
   int n = 0;

	if(DEBUG){
		printf("line_builder\n");
	}

   do {
        c = fgetc(fp);
        if(c == 'a' || c == 'b' || c == 'c' || c == 'd' || c == 'e' ||
	   c == 'f' || c == 'g' || c == 'h' || c == 'i' || c == 'j' ||
	   c == 'k' || c == 'l' || c == 'm' || c == 'n' || c == 'o' ||
	   c == 'p' || c == 'q' || c == 'r' || c == 's' || c == 't' ||
	   c == 'u' || c == 'v' || c == 'w' || c == 'x' || c == 'y' ||
	   c == 'z' || c == 'A' || c == 'B' || c == 'C' || c == 'D' ||
	   c == 'E' || c == 'F' || c == 'G' || c == 'H' || c == 'I' ||
	   c == 'J' || c == 'K' || c == 'L' || c == 'M' || c == 'N' ||
	   c == 'O' || c == 'P' || c == 'Q' || c == 'R' || c == 'S' ||
	   c == 'T' || c == 'U' || c == 'V' || c == 'W' || c == 'X' ||
	   c == 'Y' || c == 'Z' || c == '0' || c == '1' || c == '2' ||
	   c == '3' || c == '4' || c == '5' || c == '6' || c == '7' ||
	   c == '8' || c == '9' || c == '>') {
	        str[n] = (char)c;
        	n++;
		if (n > 4000) {
			break;
		}
        }
	else {
		break;
	}
   } while(1);
   str[n]='\r';
   n++;
   str[n]='\n';
//   str[n++]='\0';
   ret=str;
   return ret;
}

int main(int argc, char *argv[])
{
	FILE *atcmds;
	FILE *modem;
	FILE *output;
	char *line;
//	bool success;
	int res;

	while (true) {
		int option_index = 0;
		int c;

		c = getopt_long(argc, argv, short_options, long_options, &option_index);
		if (c == -1) {
			break;
		}
		switch (c) {
		case 'h':
			help(argv[0]);
			return EXIT_SUCCESS;
		case 'V':
			printf("atinout version " VERSION "\n");
			if (argc == 2) {
				printf("Copyright (C) 2013 Håkon Løvdal <hlovdal@users.sourceforge.net>\n"
				       "This program comes with ABSOLUTELY NO WARRANTY.\n"
				       "This is free software, and you are welcome to redistribute it under\n"
				       "certain conditions; see http://www.gnu.org/licenses/gpl.html for details.\n");
				return EXIT_SUCCESS;
			}
			break;
		case 0:
			if (strcmp("usage", long_options[option_index].name) == 0) {
				usage(argv[0]);
				return EXIT_SUCCESS;
			}
			break;
		case '?':
			break;
		default:
			fprintf(stderr, "getopt returned character code 0x%02x\n", (unsigned int)c);
		}
	}

	if ((argc - optind) != 3) {
		usage(argv[0]);
		return EXIT_FAILURE;
	}

#define INPUT_FILE   argv[optind + 0]
#define MODEM_DEVICE argv[optind + 1]
#define OUTPUT_FILE  argv[optind + 2]

	if (strcmp(INPUT_FILE, "-") == 0) {
		atcmds = stdin;
	} else {
		atcmds = fopen(INPUT_FILE, "rb");
		if (atcmds == NULL) {
			fprintf(stderr, "fopen(%s) failed: %s\n", INPUT_FILE, strerror(errno));
			return EXIT_FAILURE;
		}
	}

	modem = fopen(MODEM_DEVICE, "r+b");
	if (modem == NULL) {
		fprintf(stderr, "fopen(%s) failed: %s\n", MODEM_DEVICE, strerror(errno));
		return EXIT_FAILURE;
	}

	if (strcmp(OUTPUT_FILE, "-") == 0) {
		output = stdout;
	} else {
		output = fopen(OUTPUT_FILE, "wb");
		if (output == NULL) {
			fprintf(stderr, "fopen(%s) failed: %s\n", OUTPUT_FILE, strerror(errno));
			return EXIT_FAILURE;
		}
	}

	goto start;
	while (line != NULL) {
/*                success = tr_lf_cr(line);
                if (! success) {
                        fprintf(stderr, "invalid string: '%s'\n", line);
                        return EXIT_FAILURE;
                }*/
		res = fputs(line, modem);
		if (res < 0) {
			fprintf(stderr, "failed to send '%s' to modem (res = %d)\n", line, res);
			return EXIT_FAILURE;
		}
		do {
			if(DEBUG){
				printf("do\n");
			}

			line = line_builder(modem);
			if(DEBUG){
				printf(line);
			}
			if (line == NULL) {
				fprintf(stderr, "EOF from modem\n");
				return EXIT_FAILURE;
			}
			if(DEBUG){
				printf("line!NULL\n");
			}
			strcpy(buf, line);
			if(DEBUG){
				printf("strcpy finished\n");
			}
//			strip_cr(buf);
			res = fputs(buf, output);
			if (res < 0) {
				fprintf(stderr, "failed to write '%s' to output file (res = %d)\n", buf, res);
				return EXIT_FAILURE;
			}
		} while (! is_final_result(line));
start:
		if(DEBUG){
			printf("while\n");
		}
		line = line_builder(atcmds);
		if (line == "\r\n") {
			line = NULL;
		}
	}

	if (strcmp(OUTPUT_FILE, "-") != 0) {
		res = fclose(output);
		if (res != 0) {
			fprintf(stderr, "closing output failed: %s\n", strerror(errno));
			return EXIT_FAILURE;
		}
	}
	res = fclose(modem);
	if (res != 0) {
		fprintf(stderr, "closing modem failed: %s\n", strerror(errno));
		return EXIT_FAILURE;
	}
	if (strcmp(INPUT_FILE, "-") != 0) {
		res = fclose(atcmds);
		if (res != 0) {
			fprintf(stderr, "closing input failed: %s\n", strerror(errno));
			return EXIT_FAILURE;
		}
	}
	return EXIT_SUCCESS;
}

