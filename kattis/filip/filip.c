#include <stdio.h>

int to_int(char *p)
{
    int n = 0;
    while (*p) {
        n = n * 10 + *p - '0';
        p++;
    }
    return n;
}

void swap(char *p)
{
    char temp = *p;
    *p = p[2];
    p[2] = temp;
}

int main()
{
    char a[4], b[4];
    scanf("%s %s", a, b);
    swap(a), swap(b);
    printf("%s\n", (to_int(a) > to_int(b)) ? a : b);
    return 0;
}