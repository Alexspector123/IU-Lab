#include<stdio.h>
#include<math.h>
double Try(int n)
{
    double pi=0;
    for(int i=1;i<=n;i++)
        pi+=1/pow(i,2);
    return (sqrt(6*pi));
}
int main()
{
    int n,x;
    for(int i=10000;i<=20000;i+=1000)
    printf("%d %.4llf\n",i,Try(i));
}
