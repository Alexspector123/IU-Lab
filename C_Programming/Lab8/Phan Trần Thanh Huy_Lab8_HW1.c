#include<stdio.h>
int main()
{
    int x=2, y=8;
    int *p=&x, *q=&y;
    printf("The address of x and the value of x is: %p %d\n",&x,x);
    printf("The value of p and the value of *p is: %p %d\n",p,*p);
    printf("The address of y and the value of y is: %p %d\n",&y,y);
    printf("The value of q and the value of *q is: %p %d\n",q,*q);
    printf("The address of p is: %p\n",&p);
    printf("The address of q is: %p",&q);
}
