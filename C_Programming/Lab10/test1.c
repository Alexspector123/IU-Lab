#include<stdio.h>
#include<stdlib.h>
#include<string.h>
void Input(int a[][100],int b,int c, int m, int n)
{
    for(int i=0;i<m;i++)
        for(int j=0;j<n;j++)
        a[i][j]=b+(rand()%c);
}
void Output(int a[][100], int m, int n)
{
    for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
                printf("%d ",a[i][j]);
            printf("\n");
        }
}
int main()
{
    srand(time(NULL));
    int a[100][100],b,c,m,n;
    scanf("%d %d %d %d",&m,&n,&b,&c);
    Input(a,b,c,m,n);
    Output(a,m,n);
}
