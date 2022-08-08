#ifndef MY_LIBRARY_H
#define MY_LIBRARY_H

#include <stdbool.h>

typedef struct my_struct_t my_struct_t;

my_struct_t * lib_test_init(char const * str);
void lib_do_something(bool t, my_struct_t * val);
char const * lib_test_get_str(my_struct_t * val);

#endif
