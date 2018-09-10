#include <stdio.h>

int main()
{
    int n, m, r, s;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &m);
        scanf("%d", &r);
        while (--m) {
            scanf("%d", &s);
            r ^= s;
        }
        printf("Case #%d: %d\n", i + 1, r);
    }
}
