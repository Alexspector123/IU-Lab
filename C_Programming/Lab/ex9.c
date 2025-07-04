#include <stdio.h>
#include <stdlib.h>

int compare(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}
int isSumToMax(int a[], int size) {
    qsort(a, size, sizeof(int), compare);
    int max = a[size - 1];
    for (int i = size - 2; i >= 0; --i) {
        if (max - a[i] < 0)
            return 0;
        max -= a[i];
    }
    if (max == 0)
        return 1;
    return 0;
}



int main() {
    int n;
    scanf("%d", &n);
    int* a = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) {
        scanf("%d", &a[i]);
    }
    printf("%d", isSumToMax(a, n));
    free(a);
    return 0;
}
