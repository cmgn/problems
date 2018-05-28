#include <stdio.h>

int main()
{
  int n, x, y, a, b;
  scanf("%d %d %d", &x, &y, &n);
  for (int i = 1; i <= n; i++) {
    a = !(i % x), b = !(i % y);
    if (a && b)
      puts("FizzBuzz");
    else if (a)
      puts("Fizz");
    else if (b)
      puts("Buzz");
    else
      printf("%d\n", i);
  }
  return 0;
}