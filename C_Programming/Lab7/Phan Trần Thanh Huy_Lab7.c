#include<stdio.h>
void reset(int a, int b, int c[][100])
{
    for(int i=0; i<a; i++)
        for(int j=0; j<b; j++)
            c[i][j]=0;
}
void Input(int a, int b, int c[][100])
{
    for(int i=0; i<a; i++)
        for(int j=0; j<b; j++)
            scanf("%d",&c[i][j]);
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
void randomInput(int m, int n, int a, int b, int c[][100])
{
    for(int i=0;i<m;i++)
        for(int j=0;j<n;j++)
            c[i][j]=a+(rand()%(b-1));
}
int identical(int m,int n, int a, int b, int z[][100], int c[][100])
{
    if(m!=a || n!=b)
        return 0;
    else
    {
    for(int i=0;i<m;i++)
        for(int j=0;j<n;j++)
        if(c[i][j]!=z[i][j])
        return 0;
    return 1;
    }
}
void MainDiagonal(int n, int c[][100])
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
void SecondDiagonal(int n, int c[][100])
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
int symmetric1(int n, int c[][100])
{
    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++)
            if(c[i][j]!=c[j][i])
                return 0;
    return 1;
}
int symmetric2(int n, int c[][100])
{
    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++)
            if(c[i][j]!=c[n-1-j][n-1-i])
                return 0;
    return 1;
}
void Transpose(int m, int n, int c[][100])
{
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        printf("%d ",c[j][i]);
        printf("\n");
    }
}
void multiple(int m, int n, int b, int d[][100], int e[][100], int f[][100])
{
    for(int i=0;i<m;i++)
        for(int j=0;j<b;j++)
            for(int k=0;k<n;k++)
            f[i][j]+=d[i][k]*e[k][j];
}
int main()
{
    printf("This is the lab of two-dimensional array\n Choose the Items:\n");
    printf("1.Input the Array!\n");
    printf("2.Output the Array!\n");
    printf("3.Randomize the Array!\n");
    printf("4.Check the identical Array!\n");
    printf("5.Sort the Array!\n");
    printf("6.Check the symmetric Array with respect to the main diagonal!\n");
    printf("7.Check the symmetric Array with respect to the second diagonal!\n");
    printf("8.Transpose the matrix!\n");
    printf("9.Multiply 2 matrices!\n");
    printf("10.Reset!\n");
    int t;
    scanf("%d",&t);
    int c[100][100];
    int m,n;
    while (t!=0)
    {
        if(t==1)
        {
            printf("Enter the numer of rows and columns: ");
            scanf("%d %d",&m,&n);
            Input(m,n,c);
        }
        else if(t==2)
        {
            Output(m,n,c);
        }
        else if(t==3)
        {
            int a,b;
            printf("Enter the range of rows and columns: ");
            scanf("%d %d",&m,&n);
            printf("Enter the range for randomize: ");
            scanf("%d %d",&a,&b);
            randomInput(m,n,a,b,c);
        }
        else if(t==4)
        {
            int a,b;
            int z[100][100];
            printf("Enter the numer of rows and columns for the second Array: ");
            scanf("%d %d",&a,&b);
            Input(a,b,z);
            if(identical(m,n,a,b,z,c)) printf("It is a identity matrix!\n");
            else printf("It is not a identity matrix!\n");
        }
        else if(t==5)
        {
            if(m!=n)
                printf("This function applying for square matrix!\n Please try again!\n");
            else
            {
                MainDiagonal(n,c);
                SecondDiagonal(n,c);
            }
        }
        else if(t==6)
        {
            if(m!=n)
                printf("This function applying for square matrix!\n Please try again!\n");
            else
            {
                if(symmetric1(n,c)) printf("This matrix is symmetric with respect to the main diagonal!\n");
                else printf("This matrix is not symmetric with respect to the main diagonal!\n");
            }
        }
        else if(t==7)
        {
            if(m!=n)
                printf("This function applying for square matrix!\n Please try again!\n");
            else
            {
                if(symmetric2(n,c)) printf("This matrix is symmetric with respect to the second diagonal!\n");
                else printf("This matrix is symmetric with respect to the second diagonal!\n");
            }
        }
        else if(t==8)
        {
            Transpose(m,n,c);
        }
        else if(t==9)
        {
            int a,b;
            int z[100][100];
            printf("Enter the numer of rows and columns for the second Array: ");
            scanf("%d %d",&a,&b);
            Input(a,b,z);
            int y[100][100];
            if(n!=a)
                printf("Cannot calculate the multiplication");
            else
            {
                multiple(m,n,b,c,z,y);
                Output(m,b,y);
            }
        }
        else if(t==10)
        {
            reset(m,n,c);
        }
        printf("Do you want to continue your selection?\n");
        scanf("%d", &t);
    }
}
