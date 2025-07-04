#include<stdio.h>

int main()
{
    int a,b;
    printf("Enter two number:");
    scanf("%d %d",&a,&b);
    if(a==b)
        printf("They are equal");
    else
    {
        if(a>b)
            printf("%d is the larger number",a);
        else printf("%d is the larger number",b);
    }
}
