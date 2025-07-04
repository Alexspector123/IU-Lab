#include<stdio.h>
#include<stdlib.h>
typedef struct Num
{
    int num;
    char *name;
    char *ten;
} Num;
int main()
{
    const char *name[]= {"","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Ninteen"};
    const char *ten[]= {"","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"};
    int n;
    scanf("%d",&n);
    Num a[20];
    for(int i=0; i<=19; i++)
        a[i].num=i;
    for(int i=0; i<=19; i++)
        a[i].name=name[i];
    for(int i=0; i<=9; i++)
        a[i].ten=ten[i];
    if(n<=19)
    {
        for(int i=0; i<=19; i++)
            if(a[i].num==n)
                printf("%s",a[i].name);
    }
    else
    {
        int b[10],m=0;
        while(n!=0)
        {
            b[m]=n%10;
            n/=10;
            m++;
        }
        for(int i=m-1; i>=0; i--)
        {
            if((i==1) || (i==4)) printf("%s ",a[b[i]].ten);
            else
            {
                printf("%s ",a[b[i]].name);
            }
            if((i==2) || (i==5)) printf("hundred ");
            if(i==3) printf("thoundsand ");
        }
    }
}
