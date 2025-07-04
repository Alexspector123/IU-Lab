#include<stdio.h>
#include<math.h>

double Try(double x,int n)
{
    if(n==0)
        return x;
    return Try(sqrt(x),n-1);
}
int main()
{
    int n;
    double x;
    scanf("%d%lf",&n,&x);
    printf("%lf",Try(x,n));
}
