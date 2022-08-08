#include <stdio.h>

void func(int i, int * val){
printf("%p\n", val + i);
printf("%d=%d\n", i, val[i]);
}

int * func2(){ // let's return a pointer from this function
int a = 4711;
return & a;
}

void fun(int * a, int * b){
*a = *a + *b;
}

int main(int argc, char ** argv){
int v = 4711;
func(0, & v); // what does this print, if valid ?

int arr[] = {1,2,3,4};
func(3, arr); // what does this print, if valid ?
func(4, arr); // what does this print, if valid ?
func(-1, arr); // what does this print, if valid ?

func(0, v); // what does this print, if valid ?

int * p = func2();
printf("%d\n", *p); // what does this print, if valid ?

int c = 10;
fun(&c, &c); // what does this do, if valid ?
printf("%d\n", c);

return 0;
}


//This is the output of broken.c:

//broken.c: In function ‘func2’:
//broken.c:10:8: warning: function returns address of local variable [-Wreturn-local-addr]
//return & a;
//       ^
//broken.c: In function ‘main’:
//broken.c:26:9: warning: passing argument 2 of ‘func’ makes pointer from integer without a cast [-Wint-conversion]
//func(0, v); // what does this print, if valid ?
//        ^
//broken.c:3:6: note: expected ‘int *’ but argument is of type ‘int’
//void func(int i, int * val){
//     ^
