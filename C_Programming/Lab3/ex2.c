#include <stdio.h>

void Combination(int amount)
{
    for(int i = 0; i<=amount/10000; i++)
        for(int j = 0; j <= (amount-10000*i)/5000; j++)
            for(int k = 0;k<=(amount-5000*j-10000*i)/2000; k++)
                for(int l = 0; l <= (amount-i*10000-j*5000-k*2000)/1000; l++)
                    if((i*10000 + j*5000 + k*2000 + l*1000) == amount)
                         printf("%d x 10000 VND + %d x 5000 VND + %d x 2000 VND + %d x 1000 VND\n",i, j,k,l);
}
int main(){
    int n;
    printf("Enter the money: ");
    scanf("%d",&n);
    Combination(n);
}
