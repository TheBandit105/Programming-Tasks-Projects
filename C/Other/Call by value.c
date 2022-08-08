#include <stdio.h>

void f2call_by_value(int p){
printf("2 position: %p\n", & p);
}

void f1call_by_value(int p){
printf("1 position: %p\n", & p);
}


int main(int argc, char ** argv){
int x = 8;
printf("x position: %p\n", & x);
f1call_by_value(x);
return 0;
}
