#include <stdio.h>
#include <stdlib.h>
#include "siny.h"

int main(int argc, char * argv[])
{
 if (argc != 3) {
  printf ("Usage: %s n m (with n and m integers)\n", argv[0]);
  exit (EXIT_SUCCESS);
 }
 
 int n = atoi(argv[1]);
 int m = atoi(argv[2]);
 double result = siny(n,m);

 printf("y = sin(%d*pi) is %1.3f\n", 2*n*m, result);

 return 0;
}

