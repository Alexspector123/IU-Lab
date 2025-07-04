#include<stdio.h>
void swapValue (int *a,int *b,int *c)
{
    int d=*c;
    *c=*a;
    *a=*b;
    *b=d;
}
int main()
{
    int x=1, y=2, z=3;
    int *p=&x, *q=&y, *r=&z;
    printf("The values of x, y, z, p, q, r, *p, *q, *r before swap: %d %d %d %p %p %p %d %d %d\n",x,y,z,p,q,r,*p,*q,*r);
    swapValue(&x,&y,&z);
    printf("The values of x, y, z, p, q, r, *p, *q, *r after swap: %d %d %d %p %p %p %d %d %d",x,y,z,p,q,r,*p,*q,*r);
}
