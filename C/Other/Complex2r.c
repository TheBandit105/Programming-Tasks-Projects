#include <stdio.h>
#include <stdlib.h>

int func(int i, int n){
  int sum = 0;
  for (int j = 0; j < n; j++){
    sum = sum + i * j;
  }
  return sum;
}

int main(int argc, char ** argv){
  int n = atoi(argv[1]);
  int sum = 0;
  for (int i = 0; i < n; i++){
    sum += func(i, n);
  }
  printf("%d\n", sum);
  return 0;
}
