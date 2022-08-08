#include <stdio.h>

int g_var = 4; // Set GLOBAL variable of 4

int f1(int p){
  int g_var = 4;
  g_var += p;
  return p + g_var;
}

static int f2(int p){
  g_var += p;
  return p + g_var;
}

int main(int argc, char ** argv){
  int x = 8;
  for(int i = 0; i < 4; i++){
    printf("i=%d\n", i);
    printf("f1 value: %d\n", f1(i));
    printf("f2 value: %d\n", f2(i));
  }
  return 0;
}
