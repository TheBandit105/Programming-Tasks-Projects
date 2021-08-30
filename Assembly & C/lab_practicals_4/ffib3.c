#include <stdio.h>
#include <stdlib.h>

int fib (int n)
{
	int x, y;
	if (n < 2) return n;
	else {
		x = fib (n-1);
		y = fib (n-2);
		return x + y;
	}
}

