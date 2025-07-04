#include <stdio.h>
#include <math.h>
int main()
{
    float a, b, c;
    printf("Enter a, b, c respectively: ")
    scanf("%f%f%f", &a, &b, &c);
    if(a == 0) {
        if(b == 0) {
            if(c == 0) printf("The equation has infinitely many solutions");
            else printf("The equation has no solution");
        }
        else {
            float x = -c / b;
            printf("The solution of the equation: x = %f", x);
        }
    }
    else {
        float delta = pow(b, 2) - 4. * a * c;
        if(delta < 0) printf("The equation has no real solution");
        if(delta == 0) {
            float x = - b / 2. * a;
            printf("The equation has a double solution: x = %f", x);
        }
        else {
            float x1 = (-b + sqrt(delta)) / (2. * a);
            float x2 = (-b - sqrt(delta)) / (2. * a);
            printf("the equation has two solutions:\nx1 = %f\nx2 = %f", x1, x2);
        }
    }
    return 0;
}
