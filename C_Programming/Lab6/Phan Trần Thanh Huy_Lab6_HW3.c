#include<stdio.h>
void input(int a[], int n)
{
    for(int i=0;i<n;i++)
        scanf("%d",&a[i]);
}
void output(int a[],int n)
{
    for(int i=0;i<n;i++)
        printf("%d ",a[i]);
}
int min(int a[],int n)
{
    int m=a[0],j=0;
    for(int i=1;i<n;i++)
        if(m>a[i])
        {
            m=a[i];
            j=i;
        }
    return j;
}
int max(int a[],int n)
{
    int m=a[0],j=0;
    for(int i=1;i<n;i++)
        if(m<a[i])
        {
            m=a[i];
            j=i;
        }
    return j;
}
int main()
{
    int n;
    printf("Enter the n number: ");
    scanf("%d",&n);
    int a[n];
    printf("Enter the array: ");
    input(a,n);
    printf("Index of min element is: %d\n",min(a,n));
    printf("Index of max element is: %d",max(a,n));
}
