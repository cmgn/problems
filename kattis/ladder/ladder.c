#include <math.h>
#include <stdio.h>

int main()
{
    int h, v;
    scanf("%d %d", &h, &v);
    printf("%d\n", (int) ceil(h / sin(v * M_PI / 180)));
    return 0;
}