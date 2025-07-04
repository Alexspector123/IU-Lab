#include<stdio.h>

int main()
{
    int n;
    int max=-1000006,min=1000006;
    float average=0;
    long long product=1;
    int t;
    printf("Enter numbers:");
    scanf("%d",&n);
    while(n!=0)
    {
        if(n<min) min=n;
        if(n>max) max=n;
        average+=n;
        t++;
        product*=n;
        scanf("%d",&n);
    }
    printf("The max of all numbers: %d\n",max);
    printf("The min of all numbers: %d\n",min);
    printf("The average of all numbers: %f\n",average/t);
    printf("The product of all numbers: %lld\n",product);
}
