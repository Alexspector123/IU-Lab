#include<stdio.h>
int m, n;
void Input(int a, int b, int c[][n])
{
    for(int i=0;i<m;i++)
        for(int j=0;j<n;j++)
            scanf("%d",&c[i][j]);
}
int Check(int c[][n])
{
    for(int i=0;i<m;i++)
        for(int j=0;j<n;j++)
        if((i==j && c[i][j]!=1) ||(i!=j && c[i][j]==1))
        return 0;
    return 1;
}
int main()
{
    int a,b;
    scanf("%d %d",&m,&n);
    srand(time(NULL));
    int c[m][n];
    Input(a,b,c);
    if(Check(c)) printf("It is a identity matrix!");
    else printf("It is not a identity matrix!");
}

