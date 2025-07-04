#include<stdio.h>
#include<math.h>
#include<stdbool.h>

int main()
{
    const int N=1000;
    bool prime[N];
    int i,j;
    for(i=2; i<=N; i++)
        prime[i]=true;
    for(i=2; i<=N; i++)
        for(j=i; j<=N/i; j++)
            if(prime[i*j])
                prime[i*j]=false;
    int n;
    scanf("%d",&n);
    for(i=2; i<n; i++)
        if(prime[i])
            printf("%d ",i);
}
