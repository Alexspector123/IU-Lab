#include<stdio.h>
#include<math.h>
#include<stdbool.h>
bool Prime(int a)
{
    for(int i=2;i<=sqrt(a);i++)
        if(a%i==0)
        return false;
    return true;
}
bool Perfect(int a)
{
    int b=0;
    for(int i=1;i<=a/2;i++)
        if(a%i==0)
        b+=i;
    if(b==a) return true;
    return false;
}
int main()
{
    int n;
    for(int i=1;i<=1000;i++)
        if(Prime(i)) printf("%d ",i);
    else if(Perfect(i)) printf("%d ",i);
}


