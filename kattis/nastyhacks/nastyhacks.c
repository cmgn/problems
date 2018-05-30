#include <stdio.h>

int main()
{
    int n, r, e, c;
    scanf("%d", &n);
    while (n--) {
        scanf("%d %d %d", &r, &e, &c);
        if (e - c > r)
            puts("advertise");
        else if (e - c == r)
            puts("does not matter");
        else
            puts("do not advertise");
    }
    return 0;
}
