#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <unistd.h>

int main() {
	pid_t pid;

	pid = fork();
	if (pid < 0) {
		fprintf(stderr, "Fork Failed\n");
		exit(-1);
	}
	if (pid == 0) {
		execlp("/bin/ls", "ls", "-l", "/home", NULL);
	} else {
		wait(NULL);
		printf("Child Complete\n");
		exit(0);
	}
}
