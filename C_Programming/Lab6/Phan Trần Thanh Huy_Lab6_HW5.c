#include<stdio.h>
void input(int a[], int n)
{
    for(int i=0;i<n;i++)
        scanf("%d",&a[i]);
}
void moving(int a[], int n)
{
    for(int i=0;i<n;i++)
        if(a[i]>0)
    {
        while(a[i-1]<0)
        {
            int temp=a[i];
            a[i]=a[i-1];
            a[i-1]=temp;
            i--;
        }
    }
}
void output(int a[],int n)
{
    for(int i=0;i<n;i++)
        printf("%d ",a[i]);
}
int main()
{
    int n;
    printf("Enter the n number: ");
    scanf("%d",&n);
    int a[n];
    printf("Enter the array: ");
    input(a,n);
    moving(a,n);
    output(a,n);
}
