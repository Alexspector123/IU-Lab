#include<stdio.h>

int main()
{
    int n;
    printf("Enter the number: ");
    scanf("%d",&n);
    if(n==0)
        printf(0);
    else
    {
        while(n>0)
        {
            printf("%d ",n%10);
            n/=10;
        }
    }

}
