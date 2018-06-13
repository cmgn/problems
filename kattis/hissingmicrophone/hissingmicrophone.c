#include <stdio.h>

int contains_ss(char *p)
{
    while (*p && (*p + 1)) {
        if (*p == 's' && *(p + 1) == 's') {
            return 1;
        }
        p += 1;
    }
    return 0;
}

int main()
{
    char buffer[31];
    scanf("%s", buffer);
    if (contains_ss(buffer)) {
        printf("hiss\n");
    } else {
        printf("no hiss\n");
    }
    return 0;
}
