#include <stdio.h>
#include <string.h>

void reverse(char word[50]) {

    int word_length = strlen(word);

    int i;

    for (i = word_length; i >= 0; i--){
        printf("%c", word[i]);
    }
    printf("\n");
    
}


int main() {

    char user_word[50];

    printf("What word would you like to reverse? ");

    scanf("%s", user_word);

    reverse(user_word);
    
    return 0;
}