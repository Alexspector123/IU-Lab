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
int symmetric(int c[][n])
{
    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++)
            if(c[i][j]!=c[j][i])
                return 0;
    return 1;
}
int main()
{
    scanf("%d",&n);
    int c[n][n];
    Input(c);
    if(symmetric(c)) printf("True");
    else printf("False");
}

