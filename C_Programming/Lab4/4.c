#include <stdio.h>
#include<math.h>
#define ll long long
int main()
{
    ll n;
    scanf("%lld",&n);
    ll test=0;
    int digit=0;
    while(n-test>0)
        {
        digit++;
        test=test+pow(10,digit-1)*9*digit;
        }
    ll a=(n-test)/digit;
    ll b=(n-test)%digit;
    ll c=a+pow(10,digit-1);
    printf("%lld",a);
    if(b==0)
        c--;
    if(b!=0)
        while(b!=digit)
    {
        c/=10;
        digit--;
    }

}
