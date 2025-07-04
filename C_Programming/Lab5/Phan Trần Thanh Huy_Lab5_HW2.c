#include<stdio.h>
#include<math.h>
long long Pow(int a, int b)
{
    long long c=1;
    for(int i=1;i<=b;i++)
        c*=a;
    return c;
}
int Try(int n, int x)
{
    long long sum=0;
    for(int i=1;i<=n;i++)
        sum+=Pow(x,i);
    return sum;
}
int main()
{
    int n,x;
    scanf("%d %d",&n,&x);
    printf("%lld",Try(n,x));

}

