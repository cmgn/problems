#include <stdio.h>

int main()
{
    int t, s, d, a, b;
    scanf("%d", &t);
    while (t--) {
        scanf("%d %d", &s, &d);
        int a = (s + d) / 2;
        int b = s - a;
        if (b < 0 || a * 2 != s + d) 
            puts("impossible");
        else 
            printf("%d %d\n", a, b);
    }
    return 0;
}