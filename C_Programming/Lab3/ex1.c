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
    printf("Number  Square   Cube\n");
    for(int i=0;i<=n;i++)
    {
        long long square, cube;
        square=i*i;
        cube=i*i*i;
        printf("%d       %d        %d\n",i,square,cube);
    }
}
