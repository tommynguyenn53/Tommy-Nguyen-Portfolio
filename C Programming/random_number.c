#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {

    time_t t;
    srand((unsigned int)time(&t));  
    
    int randomNumber = rand() % 21;  
    int guesses = 5;
    int number_guessed = 0;

    printf("This is a guessing game.\nI have chosen a number between 0 and 20 which you must guess.\n");

    while(guesses > 0) {

        printf("\nYou have %d tries left.\n", guesses);
        printf("Enter a guess: ");
        scanf("%d", &number_guessed);

        if (number_guessed == randomNumber) {
            printf("Congratulations. You have guessed it!\n");
            break;
        } else if (number_guessed < randomNumber) {
            printf("Sorry %d is wrong. My number is greater than that.\n", number_guessed);
        } else if (number_guessed > randomNumber) {
            printf("Sorry %d is wrong. My number is less than that.\n", number_guessed);
        }
        
        guesses--;
    }

    if (guesses == 0) {
        printf("Sorry, you have run out of guesses.\nThe number was: %d.\n", randomNumber);
    }

    return 0;
}
