#include<stdio.h>

int main()
{
    int n;
    scanf("%d",&n);
    while(n%10!=0)
    {
        printf("%d ",n%10);
        n/=10;
    }
}
