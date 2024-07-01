#include <stdio.h>

int main() {

    
    double miniutes = 0;


    printf("How many minutes would you like to convert into years and days? ");

    scanf("%lf", &miniutes);


    double years = miniutes / (60 * 24 * 365);
    double days = ((miniutes / 60) / 24);

    printf("%lf minutes = %lf years %lf days\n", miniutes, years, days);




    return 0;
}