#include <stdio.h>
#include <stdlib.h>

int main(int argc, char * argv[])
{
 if (argc != 3) {
 printf("Usage: ./nm_adder n m (with n and m integers)\n");
 exit (EXIT_SUCCESS);
 }

 int n = atoi(argv[1]);
 int m = atoi(argv[2]);
 int result = n + m;

 printf("%d + %d = %d\n", n, m, result);

 return 0;
}
