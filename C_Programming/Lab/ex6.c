#include<stdio.h>

int main()
{
    int n;
    int s=0;
    printf("Enter n:");
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
        s+=i*i;
    printf("The value of S is: %d",s);
}
