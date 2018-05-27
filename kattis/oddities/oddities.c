#include <stdio.h>

int main()
{
  int n, m;
  scanf("%d", &n);
  while (n--) {
    scanf("%d", &m);
    if (m & 1) 
      printf("%d is odd\n", m);
    else
      printf("%d is even\n", m);
  }
  return 0;
}