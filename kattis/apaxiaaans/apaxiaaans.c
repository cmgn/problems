#include <stdio.h>

int main()
{
    char input[256] = {0};
    char output[256] = {0};
    scanf("%s", input);

    char *p = input;
    int pos = 0;

    while (*p) {
    output[pos++] = *p;
    while (*p && *p == *++p);
    }

    printf("%s\n", output);
    return 0;
}
