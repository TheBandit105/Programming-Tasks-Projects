#include <stdio.h>
#include <lib.h>

int main(){
  my_struct_t * t = lib_test_init("Hello from Test2\n");
  lib_do_something(false, t);
  return 0;
}
