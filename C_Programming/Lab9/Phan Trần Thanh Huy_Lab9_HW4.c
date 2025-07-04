#include<stdio.h>
int main()
{
    char *s;
    s=(char*)malloc(255*sizeof(char));
    gets(s);
    char *a;
    a=(char*)calloc(255,sizeof(char));
    int n=0;
    for(int i=0;i<strlen(s);i++)
    {
        if(*(s+i)!=' ')
        {
            *(a+n)=*(s+i);
            n++;
        }
        if((*(s+i)==' ') && (*(s+i+1)!=' ') && n!=0)
        {
            *(a+n)=*(s+i);
            n++;
        }
    }
    strcpy(s,a);
    printf("%s",s);
    free(s);
    free(a);
}
