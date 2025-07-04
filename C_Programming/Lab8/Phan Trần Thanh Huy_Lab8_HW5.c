#include<stdio.h>
#include<string.h>
int main()
{
    char *s;
    s=(char*)malloc(255*sizeof(char));
    printf("Enter the string: ");
    scanf("%s",s);
    int n=strlen(s);
    printf("The reverse string: ");
    for(int i=n-1;i>=0;i--)
    printf("%c",*(s+i));
    free(s);
}


