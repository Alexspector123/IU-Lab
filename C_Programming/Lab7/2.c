#include<stdio.h>
#include<stdlib.h>
#include<time.h>
int m, n;
void randomInput(int a, int b, int c[][n])
{
    for(int i=0;i<m;i++)
        for(int j=0;j<n;j++)
            c[i][j]=a+(rand()%(b-1));
}
void Output(int c[][n])
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
    int a,b;
    scanf("%d %d",&m,&n);
    scanf("%d %d",&a,&b);
    srand(time(NULL));
    int c[m][n];
    randomInput(a,b,c);
    Output(c);
}
