#include <stdio.h>

int main() {

    enum Company {GOOGLE, FACEBOOK, XEROX, YAHOO, EBAY, MICROSOFT};

    enum Company xerox, google, ebay;
    xerox = XEROX;
    google = GOOGLE;
    ebay = EBAY;

    printf("%d\n%d\n%d\n", xerox, google, ebay);

    return 0;
}

