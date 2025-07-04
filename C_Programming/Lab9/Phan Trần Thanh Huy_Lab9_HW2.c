#include<stdio.h>
#include<string.h>
int main()
{
    int n;
    scanf("%d",&n);
    char *s[n];
    for(int i=0;i<n;i++)
    {
        s[i]=malloc(255*sizeof(char));
        scanf("%s",s[i]);
    }
    for(int i=0;i<n-1;i++)
        for(int j=i+1;j<n;j++)
        if(strcmp(s[i],s[j])>0)
    {
        char *temp=s[i];
        s[i]=s[j];
        s[j]=temp;
    }
    for(int i=0;i<n;i++)
    {
        printf("%s ",s[i]);
    }
    for(int i=0;i<n;i++)
    {
        free(s[i]);
    }
}
