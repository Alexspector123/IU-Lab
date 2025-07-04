#include<stdio.h>

int main()
{
    char ope;
    int num1, num2;
    scanf("%d%c%d",&num1,&ope,&num2);
    switch(ope)
    {
    case '+':
        printf("%d + %d = %d",num1,num2,num1+num2);
        break;
    case '-':
        printf("%d - %d = %d",num1,num2,num1-num2);
        break;
    case '*':
        printf("%d * %d = %d",num1,num2,num1*num2);
        break;
    case '/':
        printf("%d / %d = %d",num1,num2,num1/num2);
        break;
    }
}
