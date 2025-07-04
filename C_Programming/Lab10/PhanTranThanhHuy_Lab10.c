#include<stdio.h>
#include<stdlib.h>
#include<string.h>
typedef struct
{
    char *ID;
    char *Full_Name;
    char *Date_Of_Birth;
    char *Department;
    float Math;
    float English;
    float Programming;
    float Average;
    int Rank;
    char last_char;
} SV;
void ResetRank(SV *a, int size)
{
    for(int i=0; i<size; i++)
        (a+i)->Rank=i+1;
}
void swap(SV *a, SV *b)
{
    SV temp=*a;
    *a=*b;
    *b=temp;
}
float Cal_Average(float a, float b, float c)
{
    float A=1.0;
    A*=(a+b+c)/3;
    return A;
}
void Input(SV *a,int *size)
{
    a=realloc(a,(*size+2)*sizeof(SV));
    printf("Please type the infor:\n");
    printf("ID: ");
    (a+*size)->ID=(char*)malloc(255*sizeof(char));
    scanf("%s",(a+*size)->ID);
    fflush(stdin);
    printf("Full name: ");
    (a+*size)->Full_Name=(char*)malloc(255*sizeof(char));
    gets((a+*size)->Full_Name);
    for(int i=strlen((a+*size)->Full_Name); i>0; i--)
        if((a+*size)->Full_Name[i-1]==' ' || i==0)
        {
            (a+*size)->last_char = (a+*size)->Full_Name[i];
            break;
        }
    printf("Date of birth: ");
    (a+*size)->Date_Of_Birth=(char*)malloc(255*sizeof(char));
    scanf("%s",(a+*size)->Date_Of_Birth);
    printf("Department: ");
    (a+*size)->Department=(char*)malloc(255*sizeof(char));
    scanf("%s",(a+*size)->Department);
    printf("Math score: ");
    scanf("%f",&(a+*size)->Math);
    printf("English score: ");
    scanf("%f",&(a+*size)->English);
    printf("Programming score: ");
    scanf("%f",&(a+*size)->Programming);
    (a+*size)->Average = Cal_Average((a+*size)->Math,(a+*size)->English,(a+*size)->Programming);
    (a+*size)->Rank = *size+1;
    *size=*size+1;
}
void Output(SV *a, int size)
{
    if(size==0)
        printf("There is nothing in the list!");
    else
        for(int i=0; i<size; i++)
        {
            printf("No.%d. %s | %s | %s | %s | %.2f | %.2f | %.2f | %.2f | %d\n",i+1,(a+i)->ID,(a+i)->Full_Name,(a+i)->Date_Of_Birth,(a+i)->Department,(a+i)->Math,(a+i)->English,(a+i)->Programming,(a+i)->Average,(a+i)->Rank);
        }
}
void Sort(SV *a, int size)
{
    for(int i=0; i<size-1; i++)
    {
        for(int j=i+1; j<size; j++)
            if((a+i)->last_char>(a+j)->last_char)
                swap((a+i),(a+j));
    }
    for(int i=0; i<size-1; i++)
    {
        for(int j=i+1; j<size; j++)
            if((a+i)->Average<(a+j)->Average && (a+i)->last_char==(a+j)->last_char)
                swap((a+i),(a+j));
    }
    printf("All done\n");
    ResetRank(a,size);
}
SV Search(SV *a, int size)
{
    char *id;
    char *n;
    SV *b;
    b=malloc(sizeof(SV));
    id=(char*)malloc(255*sizeof(char));
    n=(char*)malloc(255*sizeof(char));
    printf("Insert ID: ");
    scanf("%s",id);
    fflush(stdin);
    printf("Insert Name: ");
    gets(n);
    for(int i=0; i<size; i++)
        if(strcmp((a+i)->Full_Name,n)==0 && strcmp((a+i)->ID,id)==0)
        {
            free(id);
            free(n);
            return *(a+i);
        }
    return *b;
}
void Edit(SV *a, int size)
{
    SV b;
    b=Search(a,size);
    if(b.last_char==NULL)
        printf("There is nothing!\n");
    else
    {
        SV *c=&b;
        for(int i=0; i<size; i++)
            if(strcmp((a+i)->Full_Name,c->Full_Name)==0 && strcmp((a+i)->ID,c->ID)==0)
            {
                printf("Please rewrite the infor:\n");
                printf("ID: ");
                scanf("%s",(a+i)->ID);
                fflush(stdin);
                printf("Full name: ");
                gets((a+i)->Full_Name);
                for(int j=strlen((a+i)->Full_Name); j>0; j--)
                    if((a+i)->Full_Name[j-1]==' ' || j==0)
                    {
                        (a+i)->last_char = (a+i)->Full_Name[j];
                        break;
                    }
                printf("Date of birth: ");
                scanf("%s",(a+i)->Date_Of_Birth);
                printf("Department: ");
                scanf("%s",(a+i)->Department);
                printf("Math score: ");
                scanf("%f",&(a+i)->Math);
                printf("English score: ");
                scanf("%f",&(a+i)->English);
                printf("Programming score: ");
                scanf("%f",&(a+i)->Programming);
                (a+i)->Average = Cal_Average((a+i)->Math,(a+i)->English,(a+i)->Programming);
            }
        Sort(a,size);
        ResetRank(a,size);
    }
}
SV *Remove(SV *a, int *size)
{
    SV b;
    b=Search(a,*size);
    if(b.last_char==NULL)
        printf("There is nothing!\n");
    else
    {
        SV *c=&b;
        SV *d;
        int count=0;
        d=malloc(sizeof(SV));
        for(int i=0; i<*size; i++)
            if(strcmp((a+i)->Full_Name,c->Full_Name)==0 && strcmp((a+i)->ID,c->ID)==0)
                continue;
            else
            {
                d=realloc(d,(count+2)*sizeof(SV));
                (d+count)->ID=(char*)malloc(255*sizeof(char));
                strcpy((d+count)->ID,(a+i)->ID);
                (d+count)->Full_Name=(char*)malloc(255*sizeof(char));
                strcpy((d+count)->Full_Name,(a+i)->Full_Name);
                (d+count)->Date_Of_Birth=(char*)malloc(255*sizeof(char));
                strcpy((d+count)->Date_Of_Birth,(a+i)->Date_Of_Birth);
                (d+count)->Department=(char*)malloc(255*sizeof(char));
                strcpy((d+count)->Department,(a+i)->Department);
                (d+count)->Math = (a+i)->Math;
                (d+count)->English = (a+i)->English;
                (d+count)->Programming = (a+i)->Programming;
                (d+count)->Average = (a+i)->Average;
                (d+count)->Rank = (a+i)->Rank;
                (d+count)->last_char = (a+i)->last_char;
                count++;
            }
        free(a);
        a=malloc(count*sizeof(SV));
        a=d;
        Output(a,1);
        *size = count;
        free(d);
        return a;
    }
}
int main()
{
    SV *a;
    a=malloc(sizeof(SV));
    int size=0;
    int n=-1;
    while(n!=0)
    {
        printf("=====\n");
        printf("Student Management\n");
        printf("1.Input data\n");
        printf("2.Output student list\n");
        printf("3.Sort student list\n");
        printf("4.Search student\n");
        printf("5.Edit student info\n");
        printf("6.Remove student from list\n");
        printf("7.Export data from file\n");
        printf("8.Import data from file\n");
        printf("0.Exit program\n");
        printf("Your Option: ");
        scanf("%d",&n);
        printf("=====\n");
        if(n==1)
            Input(a,&size);
        else if(n==2)
        {
            Output(a,size);
        }
        else if(n==3)
            Sort(a,size);
        else if(n==4)
        {
            SV b;
            b=Search(a,size);
            if(b.last_char==NULL)
                printf("There is nothing!\n");
            else
                printf("%s | %s | %s | %s | %.2f | %.2f | %.2f | %.2f | %d\n",b.ID,b.Full_Name,b.Date_Of_Birth,b.Department,b.Math,b.English,b.Programming,b.Average,b.Rank);
        }
        else if(n==5)
        {
            Edit(a,size);
        }
        else if(n==6)
        {
            SV *b;
            b=Remove(a,&size);
            Output(b,1);
        }
    }
    printf("Thank you for using my project!\n");
    printf("Have a great day!");
    free(a);
    return 0;
}
