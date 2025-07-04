#include<stdio.h>

int main()
{
    int n;
    int p=1;
    printf("Enter n:");
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
        p*=i;
    printf("The value of P is: %d",p);
}
