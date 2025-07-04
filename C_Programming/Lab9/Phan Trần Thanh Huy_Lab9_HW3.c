#include<stdio.h>
#include<string.h>
int main()
{
    char *s;
    s=(char*)malloc(255*sizeof(char));
    gets(s);
    int max=0, min=0, t=0;
    char *max_String, *min_String, *temp;
    temp=(char*)calloc(255,sizeof(char));
    max_String=(char*)calloc(255,sizeof(char));
    min_String=(char*)calloc(255,sizeof(char));
    for(int i=0;i<strlen(s);i++)
    {
        *(temp+t)=*(s+i);
        t++;
        if((*(s+i+1)==' ') || (i==strlen(s)-1))
        {
            if(t>max)
            {
                strcpy(max_String,temp);
                max=t;
            }
            if(t<min || min==0)
            {
                strcpy(min_String,temp);
                min=t;
            }
            temp=(char*)calloc(255,sizeof(char));
            t=0;
            i++;
        }
    }
    printf("%s",max_String);
    printf("\n%s",min_String);
    free(temp);
    free(s);
    free(max_String);
}
