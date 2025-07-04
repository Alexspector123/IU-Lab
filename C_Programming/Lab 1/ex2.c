#include<stdio.h>

int main()
{
    int n=1,max=0,min=0;
    while(n!=0)
    {
        scanf("%d",&n);
        if(max==0 && min==0)
        {
            max=n;
            min=n;
        }
        else
        {
            if(n>max) max=n;
            if(n<min) min=n;
        }
    }
    printf("Min: %d\n",min);
    printf("Max: %d\n",max);
}
