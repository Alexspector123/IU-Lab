#include<stdio.h>
#include<math.h>
#include<stdbool.h>
int digit(int a,int t)
{
    if(a==0)
        return 1;
    while(a>0)
    {
        a/=10;
        t++;
    }
    return t;
}
bool check(int a,int t)
{
    int sum=0,b=a;
    while(a>0)
    {
        sum+=pow(a%10,t);
        a/=10;
    }
    if(sum==b) return true;
    return false;
}
int main()
{
    int n;
    printf("Enter the number: ");
    scanf("%d",&n);
    if(check(n,digit(n,0)))
        printf("It is an Amstrong number");
    else printf("It is not an Amstrong number");
}
