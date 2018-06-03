#include <stdio.h>

const char *b10_digits = "0123456789";
char chars[32];
int xs[1000000];

__attribute__((always_inline)) int fast_get_int()
{
    int c = getc_unlocked(stdin);
    int r = 0;
    while (c >= 48 && c <= 57) {
        r = r * 10 + c - 48;
        c = getc_unlocked(stdin);
    }
    return r;
}

__attribute__((always_inline)) void fast_print_int(int n)
{
    char *p = chars;
    int m = n;
    do {
        p++;
        m /= 10;
    } while (m);
    *p = 0;
    do {
        *--p = b10_digits[n%10];
        n /= 10;
    } while (n);
    while (*p) {
        putchar_unlocked(*p++);
    }
}


int main()
{
    int n = fast_get_int(), m;
    int *p = xs;
    *p++ = fast_get_int();
    while (--n) {
        m = fast_get_int();
        if (m > *(p-1)) {
            *p++ = m;
        }
    }
    fast_print_int(p - xs);
    putchar_unlocked('\n');
    for (n = 0; n < p - xs; n++) {
        fast_print_int(*(xs + n));
        putchar_unlocked(' ');
    }
    return 0;
}