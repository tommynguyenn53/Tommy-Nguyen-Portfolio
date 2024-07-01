#include <stdio.h>

void squared(double* number) {
    *number = (*number) * (*number);
}

int main() {
    double number = 10.0;
    squared(&number);

    printf("The square is %.2lf\n", number);

    return 0;
}
