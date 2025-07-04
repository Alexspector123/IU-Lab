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
int main()
{
    int n;
    printf("Enter the n number: ");
    scanf("%d",&n);
    int a[n];
    printf("Enter the array: ");
    input(a,n);
    printf("Print the array: ");
    output(a,n);
}
