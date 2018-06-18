#include <stdio.h>

int main()
{
    int l, r;
    scanf("%d %d", &l, &r);
    if (!l && !r) {
        printf("Not a moose\n");
    } else if (l == r) {
        printf("Even %d\n", l + r);
    } else {
        printf("Odd %d\n", 2 * ((l > r) ? l : r));
    }
    return 0;
}