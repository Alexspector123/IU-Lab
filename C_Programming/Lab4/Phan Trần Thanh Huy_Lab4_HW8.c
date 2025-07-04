#include<stdio.h>

int main()
{
    int n;
    scanf("%d",&n);
    int a [100005];
    if(n==0)
    {
        printf("0");
        return 0;
    }
    else
    {
        int count=0;
        while(n>0)
        {
            count++;
            a[count]=n%2;
            n/=2;
        }
        for(int i=count;i>=1;i--)
            printf("%d",a[i]);
    }
}
