#include<stdio.h>
int main()
{
    char c[100];
    printf("Enter the word: ");
    scanf("%s",c);
    if(c[0]=='a' || c[0]=='e' || c[0]=='i' || c[0]=='o' || c[0]=='u' || c[0]=='A' || c[0]=='E' || c[0]=='I' || c[0]=='O' || c[0]=='U')
        printf("%s is a vowel",c);
    else printf("%s is a consonant",c);
}
