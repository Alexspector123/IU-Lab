#include<stdio.h>
#include<time.h>
#include<stdlib.h>
void Input(int *a, int n)
{
    for(int i=0;i<n;i++)
        *(a+i)=1+rand()%99;
}
void swap(int *a, int *b)
{
    int c=*a;
    *a=*b;
    *b=c;
}
void sort(int *a, int n)
{
    for(int i=0;i<n-1;i++)
        for(int j=i+1;j<n;j++)
        if(*(a+i)>*(a+j))
        swap((a+i),(a+j));
}
void Output(int *a, int n)
{
    for(int i=0;i<n;i++)
        printf("%d ",*(a+i));
}
int main()
{
    int n;
    int *a=(int*)malloc(n*sizeof(int));
    srand(time(NULL));
    printf("Enter n: ");
    scanf("%d",&n);
    Input(a,n);
    printf("An random array before sort: ");
    Output(a,n);
    sort(a,n);
    printf("\nAn random array after sort: ");
    Output(a,n);
    a=(int*)malloc(2*n*sizeof(int));
    Input(a,2*n);
    printf("\nAfter double n\nAn random array before sort: ");
    Output(a,n*2);
    sort(a,n*2);
    printf("\nAn random array after sort: ");
    Output(a,n*2);
    free(a);
}
