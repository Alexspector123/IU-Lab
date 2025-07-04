#include <stdio.h>
#include <math.h>
#include <stdbool.h>
int main(){
    int n;
    scanf("%d", &n);
    for(int i = 1; i <= n; i++)
    {
        bool kt=true;
        if(i > 1) {
            for(int j=2;j<=sqrt(i);j++)
                if(i%j==0)
                kt=false;
            if(kt)
                printf("%d ",i);
        }
    }
    return 0;
}
