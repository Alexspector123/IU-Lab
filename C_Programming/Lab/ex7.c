#include<stdio.h>

int main()
{
    int a,b,c,big;
    printf("Enter three number:");
    scanf("%d %d %d",&a,&b,&c);
    big = a>b ? (a > c ? a : c) : (b > c ? b : c);
    printf("\nThe biggest number is: %d",big);
}
