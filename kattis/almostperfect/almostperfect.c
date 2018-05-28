#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main()
{
  int n, m, s;
  while (scanf("%d", &n) != -1) {
    m = (int) sqrt(n) + 1, s = -n;
    for (int i = 1; i < m; i++) {
      if (n % i == 0) {
        s += i;
        if (n / i != i) s += n / i;
      }
    }
    if (s == n) printf("%d perfect\n", n);
    else if (abs(s - n) <= 2) printf("%d almost perfect\n", n);
    else printf("%d not perfect\n", n);
  }
}