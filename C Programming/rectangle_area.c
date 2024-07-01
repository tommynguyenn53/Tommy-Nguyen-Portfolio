#include <stdio.h>


int main() {
    double length = 0;
    double width = 0;

    printf("Pick a length: ");
    scanf("%lf", &length);

    printf("Pick a width: ");
    scanf("%lf", &width);

    double perimeter = 2 * length + 2 * width;

    double area = length * width;


    printf("The total perimeter of the rectangle is %.2lfm.\n", perimeter);
    printf("The total area of the rectangle is %.2lfm^2.\n", area);


    return 0;
}

// int main (int argc, char *argv[]) {

//     int numberOfArguments = argc;
//     char *argument1 = argv[0];

//     char *argument2 = argv[1];

//     printf("Number of Arguments: %d\n", numberOfArguments);
//     printf("Argument 1 is the program name: %s\n", argument1);
//     printf("Argument 2 is the command line argument: %s\n", argument2);

//     return 0;
// }