#include <stdio.h>
#include <stdlib.h>
#include "ffib.h"

int main (int argc, char *argv[])
{
	int n = atoi(argv[1]);
	int result = fib(n);
	printf ("Fibonacci of %d is %d \n", n, result);
	return 0;
}

