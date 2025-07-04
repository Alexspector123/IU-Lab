#include<stdio.h>
int n;
void Input(int c[][n])
{
    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++)
            scanf("%d",&c[i][j]);
}
void Output(int c[][n])
{
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        printf("%d ",c[i][j]);
        printf("\n");
    }
}
void MainDiagonal(int c[][n])
{
    for(int i=0;i<n-1;i++)
    {
        for(int j=i+1;j<n;j++)
            if(c[j][j]<c[i][i])
            {
                int temp=c[j][j];
                c[j][j]=c[i][i];
                c[i][i]=temp;
            }
    }
}
void SecondDiagonal(int c[][n])
{
    for(int i=n-1;i>0;i--)
    {
        for(int j=i-1;j>=0;j--)
            if(c[n-i-1][i]<c[n-j-1][j] && 2*i!=(n-1) && 2*j!=(n-1))
            {
                int temp=c[n-i-1][i];
                c[n-i-1][i]=c[n-j-1][j];
                c[n-j-1][j]=temp;
            }

    }
}
int main()
{
    scanf("%d",&n);
    int c[n][n];
    Input(c);
    MainDiagonal(c);
    SecondDiagonal(c);
    Output(c);
}

