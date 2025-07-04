#include<stdio.h>

int main()
{
    int a,b,c;
    printf("Enter three number:");
    scanf("%d %d %d",&a,&b,&c);
    printf("The sum of those three number: %d\n",a+b+c);
    printf("The product of those three number: %d\n",a*b*c);
    printf("The average of those three number: %f\n",(float)(a+b+c)/3);
    int minx,maxx;
    maxx = a>b ? (a > c ? a : c) : (b > c ? b : c);
    minx = a<b ? (a < c ? a : c) : (b < c ? b : c);
    printf("The min of those three number is: %d\n",minx);
    printf("The max of those three number is: %d\n",maxx);
}
