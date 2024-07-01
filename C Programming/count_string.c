#include <stdio.h>

int count_word(const char *word) {

    int i = 0;

    while(*word) {
        word ++;
        i++;
    }


    return i;


}



int main() {

    char word[20] = "";

    printf("Input a word in which would you like to know the length of: ");
    scanf("%s", word);

    int count_word_result = 0;

    count_word_result = count_word(word);

    printf("%d\n", count_word_result);

    return 0;
}