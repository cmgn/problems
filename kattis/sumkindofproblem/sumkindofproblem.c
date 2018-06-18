#include <stdio.h>

int main()
{
    int n, i, m;
    scanf("%d", &n);
    while (n--) {
        scanf("%d %d", &i, &m);
        printf("%d %d %d %d\n", i, m * (m + 1) / 2, m * m, m * m + m);
    }
    return 0;
}