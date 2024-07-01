#include <stdio.h>

int main() {
    int number = 99; 
    int *pointer = &number;

    printf("%p\n", &pointer); // outputs address of the pointer variable itself
    printf("%p\n", pointer);  // outputs the address stored in the pointer (address of 'number')
    printf("%d\n", *pointer); // outputs the value stored at the address the pointer is pointing to (value of 'number')

    return 0;
}
