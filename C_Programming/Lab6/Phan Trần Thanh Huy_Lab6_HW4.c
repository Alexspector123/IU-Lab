#include<stdio.h>
void input(int a[], int n)
{
    for(int i=0;i<n;i++)
        scanf("%d",&a[i]);
}
int symmectric(int a[],int i, int j)
{
    if(a[i]!=a[j]) return 1;
    if(i==0)
        return 0;
    return symmectric(a,i-1,j+1);
}
int main()
{
    int n;
    printf("Enter the n number: ");
    scanf("%d",&n);
    int a[n];
    printf("Enter the array: ");
    input(a,n);
    if(n%2==0)
    printf("%d",symmectric(a,n%2,n%2+1));
    else
        printf("%d",symmectric(a,n%2,n%2+2));
}
