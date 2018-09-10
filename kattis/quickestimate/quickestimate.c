#include <math.h>
#include <stdio.h>


int main()
{
    int n;
    scanf("%d\n", &n);
    while (n--) {
        char c;
        long int m = -1;
        do {
            scanf("%c", &c);
            m++;
        } while (c != '\n');
        printf("%ld\n", m);
    }
}
