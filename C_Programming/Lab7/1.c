#include<stdio.h>
#include<stdlib.h>
#include<time.h>
void randomInput(int m, int n, int a, int b, int c[][100])
{
    for(int i=0;i<m;i++)
        for(int j=0;j<n;j++)
            c[i][j]=a+(rand()%(b-1));
}
void Output(int m, int n, int c[][100])
{
    for(int i=0;i<m;i++)
    {
        for(int j=0;j<n;j++)
        printf("%d ",c[i][j]);
        printf("\n");
    }
}
int main()
{
    int n,m,a,b;
    scanf("%d %d",&m,&n);
    scanf("%d %d",&a,&b);
    srand(time(NULL));
    int c[100][100];
    randomInput(m,n,a,b,c);
    Output(m,n,c);
}
