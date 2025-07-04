#include<stdio.h>

int main()
{
    int n;
    printf("Enter the number: ");
    scanf("%d",&n);
    while(n<=0)
    {
        printf("N must larger than 0. Typing again: ");
        scanf("%d",&n);
    }
    for(int i=1;i<=n;i++)
    {
        for(int k=0;k<n-i;k++)
            printf(" ");
        for(int j=n-i;j<n;j++)
        printf("%d",i);
        printf("\n");
    }
}
