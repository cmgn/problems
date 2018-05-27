#include <stdio.h>

int main()
{
  int i, m = 0, w = 0, a, b, c, d, t;
  for (int i = 0; i < 5; i++) {
    scanf("%d %d %d %d", &a, &b, &c, &d);
    t = a + b + c + d;
    if (t > m) {
      m = t;
      w = i;
    }
  }
  printf("%d %d\n", w + 1, m);
  return 0;
}