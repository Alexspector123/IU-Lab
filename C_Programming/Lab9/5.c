#include<stdio.h>
#include<string.h>
typedef struct
{
    char *s;
}SV;
int main()
{

    int *a;
    a=(int*)malloc(1*sizeof(int));
    int i=0;
    scanf("%d",(a+i));
    i++;
    a=realloc(a,1);
    scanf("%d",(a+i));
    for(int j=0;j<=i;j++)
        printf("%d",*(a+i));
    free(a);
}
