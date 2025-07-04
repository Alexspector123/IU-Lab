#include<stdio.h>
#include<math.h>
int main()
{
    int n,test;
    printf("Enter the number: ");
    scanf("%d",&n);
    test=n;
    for(int i=1;i<=n/2;i++)
        if(n%i==0)
            test-=i;
    if(test==0) printf("%d is a perfect number",n);
    else printf("%d is not a perfect number",n);
}
