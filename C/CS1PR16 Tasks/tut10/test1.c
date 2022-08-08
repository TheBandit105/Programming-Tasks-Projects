#include <stdio.h>
#include <assert.h>
#include <string.h>
#include <lib-internal.h>

int main(){
  my_struct_t * t = lib_test_init("Hello World\n");
  assert(strcmp(t->str, "Hello World\n") == 0);
  lib_do_something(false, t);

  assert(strcmp(lib_test_get_str(t), "Hello World\n") == 0);
  return 0;
}
