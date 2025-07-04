#include<stdio.h>
#include<math.h>

int main()
{
    int n;
    printf("Enter the number: ");
    scanf("%d",&n);
    if(n>1)
    {
        for(int i=2; i<=sqrt(n); i++)
        {
            if(n%i==0)
            {
                printf("It is not a Prime number");
                return 0;
            }
        }
    }
    printf("It is a Prime number");
}
