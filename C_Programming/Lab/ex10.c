#include<stdio.h>

int main()
{
    int a[20];
    int sum=0,average,odd=0,even=0;
    for(int i=0;i<20;i++)
        scanf("%d",&a[i]);
    for(int i=0;i<20;i++)
    {
        if(a[i]%2==0) even++;
        else odd++;
        sum+=a[i];
    }
    average=sum/20;
    printf("%d     %d     %d     %d",sum,average,odd,even);
}
