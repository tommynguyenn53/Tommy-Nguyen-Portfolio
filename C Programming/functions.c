#include <stdio.h>
#include <math.h>

int gcd(int u, int v);
float absoluteValue(float number);
double square_root(double x);

int main()
{
    float absolute_result = 0;
    absolute_result = absoluteValue(-10.10);

    printf("Absolute result is: %.2f\n", absolute_result);

    double square_root_result = 0;
    square_root_result = square_root(121);

    if (square_root_result == -1)
    {
        printf("Can't square root a negative number hence result is %.2lf.\n", square_root_result);
    }

    else
    {
        printf("Square root result is: %.2lf\n", square_root_result);
    }

    int gcd_result = 0;

    gcd_result = gcd(150, 35);
    printf("The gcd of the 150 and 35 is %d\n", gcd_result);
}

int gcd(int u, int v)
{
    int temp;

    while (v != 0)
    {
        temp = u % v;
        u = v;
        v = temp;
    }

    return u;
}

float absoluteValue(float number)
{
    if (number < 0)
    {
        return -number;
    }

    else
    {
        return number;
    }
}

double square_root(double x)
{
    if (x < 0)
    {
        return -1;
    }

    else
    {
        return sqrt(x);
    }
}