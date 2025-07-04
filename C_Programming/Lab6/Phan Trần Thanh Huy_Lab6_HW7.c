#include<stdio.h>
void input(int a[], int n)
{
    for(int i=0;i<n;i++)
        scanf("%d",&a[i]);
}
int sorting(int a[], int n)
{
    for(int i=0;i<n-1;i++)
        for(int j=i+1;j<n;j++)
        if(a[i]>a[j])
    {
        int temp=a[i];
        a[i]=a[j];
        a[j]=temp;
    }
    return a[n-2];
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
    printf("The 2nd maxinum value is: %d",sorting(a,n));
}

