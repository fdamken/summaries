#include <stdio.h>
#include <string.h>

int main(void) {
	char buff[15];
	int pass = 0;

	printf("\nEnter password:\n");

	gets(buff);

	if (strcmp(buff, "12345678")) {
		printf("\nWrong password!\n");
	} else {
		printf("\nCorrect password!\n");
		pass = 1;
	}

	if (pass) {
		printf("\nGranting privileges to user.\n");
	}

	return 0;
}
