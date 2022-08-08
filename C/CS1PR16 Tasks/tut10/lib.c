#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <lib-internal.h>

my_struct_t * lib_test_init(char const * str){
  assert(str);
  my_struct_t* p = malloc(sizeof(my_struct_t));
  *p = (my_struct_t){
    .b = true,
    .str = strdup(str)
  };
  return p;
}

void lib_do_something(bool t, my_struct_t * val){
  assert(val);
  val->b = t;
  printf("%s", val->str);
}

char const * lib_test_get_str(my_struct_t * val){
  assert(val);
  return val->str;
}
