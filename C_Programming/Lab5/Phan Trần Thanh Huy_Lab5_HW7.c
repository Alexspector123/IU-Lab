#include<stdio.h>

int GCD(int a, int b)
{
    if(b==0)
        return a;
    return GCD(b,a%b);
}
int main()
{
    int a,b;
    scanf("%d%d",&a,&b);
    printf("%d\n%d",GCD(a,b),(a*b)/GCD(a,b));
}
