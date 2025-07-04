#include<stdio.h>
int Try(int n, int sum)
{
    for(int i=1;i<=n;i++)
        sum+=i*(i+1);
    return sum;
}
int main()
{
    int n,sum=0;
    scanf("%d",&n);
    printf("%d",Try(n,0));

}
