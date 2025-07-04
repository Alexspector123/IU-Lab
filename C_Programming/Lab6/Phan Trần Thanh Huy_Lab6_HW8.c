#include<stdio.h>
void input(int a[], int n)
{
    for(int i=0; i<n; i++)
        scanf("%d",&a[i]);
}
void duplicate(int a[], int n)
{
    int b[n],c[n],count=0;
    for(int i=0; i<n; i++)
    {
        if(b[a[i]]!=1)
        {
            c[count]=a[i];
            count++;
            b[a[i]]=1;
        }
    }
        for(int i=0; i<count; i++)
    printf("%d ",c[i]);
    }
    int main()
    {
        int n;
        printf("Enter the n number: ");
        scanf("%d",&n);
        int a[n];
        printf("Enter the array: ");
        input(a,n);
        duplicate(a,n);
    }
