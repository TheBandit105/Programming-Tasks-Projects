#include <stdio.h>
#include <stdlib.h>

int main (int argc, char ** argv){
  int n = atoi(argv[1]);
  int sum = 0;
  for (int i = 0; i < n; i++){
    sum += i * i;
  }
  printf("%d\n", sum);
  return 0;
}
