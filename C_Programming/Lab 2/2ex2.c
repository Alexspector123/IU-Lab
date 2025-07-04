#include<stdio.h>

int even(int a, long long product)
{
    for(int i=2;i<=a;i+=2)
        product*=i;
    return product;
}
int odd(int a,long long product)
{
    for(int i=1;i<=a;i+=2)
        product*=i;
    return product;
}
int main()
{
    int n;
    printf("Enter the number ");
    scanf("%d",&n);
    if(n%2==0)
        printf("n is an even number\n%d",even(n,1));
    else printf("n is an odd number\n%d",odd(n,1));
}
