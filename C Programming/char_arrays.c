#include <stdio.h>
#include <stdbool.h>

int count(const char word[]);
void concatenate(char result[], const char str1[], const char str2[]);
bool equal(const char str1[], const char str2[]);

int count(const char word[]) {
    int i = 0;
    while (word[i] != '\0') {
        i++;
    }
    return i;
}

void concatenate(char result[], const char str1[], const char str2[]) {
    int i, j;

    for (i = 0; str1[i] != '\0'; i++) {
        result[i] = str1[i];
    }

    for (j = 0; str2[j] != '\0'; j++) {
        result[i + j] = str2[j];
    }

    result[i + j] = '\0';
}

bool equal(const char str1[], const char str2[]) {
    int i = 0;
    
    while (str1[i] != '\0' && str2[i] != '\0') {
        if (str1[i] != str2[i]) {
            return false;
        }
        i++;
    }

    return str1[i] == '\0' && str2[i] == '\0';
}

int main() {
    int count_result = 0;
    count_result = count("Hello");
    printf("The length is %d.\n", count_result);

    char concatenate_result[50];
    const char word1[] = "tommy";
    const char word2[] = "ok";

    concatenate(concatenate_result, word1, word2);
    printf("%s\n", concatenate_result);

    bool equal_result = true;
    char str1[10] = "Hello";
    char str2[10] = "Hello";

    equal_result = equal(str1, str2);
    printf("%d\n", equal_result);

    return 0;
}
