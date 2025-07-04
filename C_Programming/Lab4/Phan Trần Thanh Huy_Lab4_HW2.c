#include <stdio.h>
#include <math.h>

int main(){
    int n;
    printf("Enter the number: ")
    scanf("%d", &n);
    int digit = n % 10;
    while(n > 0) {
        if((n % 10) > digit) digit = n % 10;
        n /= 10;
    }
    printf("Result: %d", digit);
    return 0;
}
