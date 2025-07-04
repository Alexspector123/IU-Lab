#include<stdio.h>
#include<math.h>

int main()
{
    float n;
    long long cost=1;
    printf("Enter the travel distance: ");
    scanf("%f",&n);
    cost=(long long)(n/2)*15000;
    if(n>30)
        {
            cost+=(long long)(fmod(n,30))*5000;
        }
    else
        cost+=(fmod(n,2))*2000/0.25;
    printf("The total cost is: %lld",cost);
}
