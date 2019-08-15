#include <string.h>
#include <stdio.h>

void foo(const char* input)
{
	char buf[10];

	strcpy(buf, input);
}

void bar(void)  // Address: 0x0100401103
{
	printf("Wrong code.\n");
}

int main(int argc, char* argv[])
{
	if (argc != 2)
	{
		printf("Please specify a string as an argument!\n");
		return -1;
	}

	foo(argv[1]);
	return 0;
}
