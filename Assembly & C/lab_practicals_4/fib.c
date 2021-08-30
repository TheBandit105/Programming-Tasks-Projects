#include <stdio.h>
#include <stdlib.h>

int fib (int n)
{
	int x, y;
	if (n < 2) return n;
	else {
		x = fib(n-1);
		y = fib(n-2);
		return x + y;
	}
}

int main (int argc, char *argv[])
{
	int n = atoi(argv[1]);
	int result = fib(n);
	printf ("Fibonacci of %d is %d \n", n, result);
	return 0;
}


