#include<stdio.h>

int main()
{
    int n,count=0;
    printf("Enter the number: ");
    scanf("%d",&n);
    while(n>0)
    {
        count++;
        n/=10;
    }
    if(count==1)
        printf("%d digit",count);
    else if(count>1) printf("%d digits",count);
}
