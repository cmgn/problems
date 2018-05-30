#include <stdio.h>
#include <math.h>

typedef long long unsigned int llu;

int main()
{
    llu n, m, t;
    scanf("%llu %llu %llu", &m, &n, &t);
    double i;
    switch (t) {
    case 1:
        i = n;
        while (--n && i / m <= 1) i *= n;
        break;
    case 2:
        i = pow(2, n); break;
    case 3:
        i = n*n*n*n; break;
    case 4:
        i = n*n*n; break;
    case 5:
        i = n*n; break;
    case 6:
        i = n * log(n)/log(2); break;
    case 7:
        i = n; break;
    }
    if (i / m > 1) puts("TLE");
    else puts("AC");
    return 0;
}