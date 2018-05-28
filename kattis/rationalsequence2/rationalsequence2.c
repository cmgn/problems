#include <stdio.h>

struct fraction {
  int d, n;
};

int main()
{
  struct fraction f = {0, 0};
  int n = 0, t;
  scanf("%d", &n);
  while (n--) {
    scanf("%d %d/%d", &t, &f.n, &f.d);
    int m = 0, path = 0;
    
    while (f.d != f.n) {
      if (f.d > f.n) {
        f.d -= f.n;
      } else {
        path |= (1 << m);
        f.n -= f.d;
      }
      m++;
    }

    int result = 1;
    for (int i = m - 1; i >= 0; i--) {
      if (path & (1 << i)) result = (result << 1) + 1;
      else result <<= 1;
    }

    printf("%d %d\n", t, result);
  }
  return 0;
}