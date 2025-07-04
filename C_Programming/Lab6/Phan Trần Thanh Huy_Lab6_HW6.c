#include<stdio.h>
void input(int a[], int n)
{
    for(int i=0;i<n;i++)
        scanf("%d",&a[i]);
}
int Prime(int t)
{
    for(int i=2;i*i<=t;i++)
        if(t%i==0)
        return 1;
    return 0;
}
void sorting(int a[], int n)
{
    for(int i=0;i<n-1;i++)
        for(int j=i+1;j<n;j++)
        if(a[i]>a[j] && Prime(a[i])==0 && Prime(a[j])==0)
    {
        int temp=a[i];
        a[i]=a[j];
        a[j]=temp;
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
    sorting(a,n);
    printf("After sorted: ");
    output(a,n);
}

