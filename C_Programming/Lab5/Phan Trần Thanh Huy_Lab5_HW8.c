#include<stdio.h>

void Try(int n)
{
    int a[100005];
    int count=0;
    while(n>0)
    {
        count++;
        a[count]=n%10;
        n/=10;
    }
    for(int i=count;i>=1;i--)
        printf("%d ",a[i]);
}
int main()
{
    int n;
    scanf("%d",&n);
    Try(n);
}
