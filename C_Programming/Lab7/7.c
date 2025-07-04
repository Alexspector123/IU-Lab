#include<stdio.h>
int m, n;
void Input(int c[][n])
{
    for(int i=0;i<m;i++)
        for(int j=0;j<n;j++)
            scanf("%d",&c[i][j]);
}
void Transpose(int c[][n])
{
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        printf("%d ",c[j][i]);
        printf("\n");
    }
}
int main()
{
    scanf("%d",&m);
    scanf("%d",&n);
    int c[m][n];
    Input(c);
    Transpose(c);
}


