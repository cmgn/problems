#include <stdio.h>
#include <math.h>

int main()
{
  int n, w, h, m;
  float hyp;
  scanf("%d %d %d", &n, &w, &h);
  hyp = sqrt(w*w + h*h);
  while (n--) {
    scanf("%d", &m);
    if (m <= hyp)
      puts("DA");
    else
      puts("NE");
  }
  return 0;
}