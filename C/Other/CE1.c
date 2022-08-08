#include <stdio.h>

int main(int argc, char ** argv){
  int i;
  int n = atoi(argv[1]);
  for (i = n; i >= 0; i -= 3){
    printf(".");
  }
}
