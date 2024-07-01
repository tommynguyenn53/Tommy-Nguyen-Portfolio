#include <stdio.h>

int main() {

    double base_rate = 12;
    double gross_pay = 0;
    double hours = 0;
    double excess = 0;
    double net_pay = 0;
    double tax = 0;

    printf("How many hours have you worked this week? ");
    scanf("%lf", &hours);

    if (hours > 40) {
        excess = hours - 40;
    }

    gross_pay = base_rate * hours + base_rate * 0.5 * excess;

    printf("Your gross pay is $%.2lf\n", gross_pay);

    if (gross_pay <= 300) {
        tax = gross_pay * 0.15;
    } else if (gross_pay <= 450) {
        tax = 300 * 0.15 + (gross_pay - 300) * 0.20;
    } else {
        tax = 300 * 0.15 + 150 * 0.20 + (gross_pay - 450) * 0.25;
    }

    net_pay = gross_pay - tax;

    printf("Your total tax is $%.2lf\n", tax);
    printf("Your net pay is $%.2lf\n", net_pay);

    return 0;
}
