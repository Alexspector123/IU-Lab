#include<stdio.h>
int m, n, p, q;
void Input(int d, int e, int f[][n])
{
    for(int i=0;i<d;i++)
        for(int j=0;j<e;j++)
            scanf("%d",&f[i][j]);
}
void Output(int d, int e, int f[][n])
{
    for(int i=0;i<d;i++)
    {
        for(int j=0;j<e;j++)
        printf("%d ",f[i][j]);
        printf("\n");
    }
}
void multiple(int a[][n], int b[][q], int c[][q])
{
    for(int i=0;i<m;i++)
        for(int j=0;j<q;j++)
            for(int k=0;k<n;k++)
            c[i][j]+=a[i][k]*b[k][j];
}
int main()
{
    scanf("%d %d",&m,&n);
    int a[m][n];
    scanf("%d %d",&p,&q);
    int b[p][q];
    if(n!=p)
        printf("Cannot calculate the multiplication");
    else
    {
        int c[m][q];
        for(int i=0;i<m;i++)
            for(int j=0;j<q;j++)
            c[i][j]=0;
        Input(m,n,a);
        Input(p,q,b);
        multiple(a,b,c);
        Output(m,q,c);
    }
}
