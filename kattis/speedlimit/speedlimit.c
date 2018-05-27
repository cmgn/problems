#include <stdio.h>

int main()
{
  int n = 0, s, t, i, elapsed, dist;
  scanf("%d", &n);
  while (n != -1) {
    dist = 0;
    elapsed = 0;
    for (i = 0; i < n; i++) {
      scanf("%d %d", &s, &t);
      dist += (t - elapsed) * s;
      elapsed = t;
    }
    printf("%d miles\n", dist);
    scanf("%d", &n);
  }
  return 0;
}