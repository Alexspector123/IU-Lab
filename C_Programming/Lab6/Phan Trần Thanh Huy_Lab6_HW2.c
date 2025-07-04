#include<stdio.h>
#include<stdlib.h>
#include<time.h>
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
void randomInRange(int a[], int n)
{
    for(int i=0;i<n;i++)
        printf("%d ",a[0]+(rand() % a[n-1]));
}
int main()
{
    int n;
    printf("Enter the n number: ");
    scanf("%d",&n);
    srand(time(NULL));
    int a[n];
    printf("Enter the array: ");
    input(a,n);
    randomInRange(a,n);
}

