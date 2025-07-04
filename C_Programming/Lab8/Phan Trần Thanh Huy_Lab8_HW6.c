#include<stdio.h>
void swap(int *a, int*b)
{
    int temp=*a;
    *a=*b;
    *b=temp;
}
int main()
{
    int n;
    printf("Enter n: ");
    scanf("%d",&n);
    int *a=(int*)malloc(n*sizeof(int));
    int t=0;
    printf("Enter the array: ");
    for(int i=0;i<n;i++)
    {
        scanf("%d",(a+i));
        if(*(a+i)%2==0)
        {
            swap(a+i,a+t);
            t++;
        }
    }
    printf("The array after segregation is: ");
    for(int i=0;i<n;i++)
        printf("%d ",*(a+i));
    free(a);
}
