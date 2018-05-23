#include <stdio.h>

typedef long long unsigned int llu;
int divisible_by_all(llu n);

const int divisors[] = {11, 13, 14, 16, 17, 18, 19, 20};
const int divisor_length = 8;

int main()
{
  llu n = 20;
  while (!divisible_by_all(n)) n += 20;
  printf("%llu\n", n);
}

int divisible_by_all(llu n)
{
  int i = 0;
  while (i < divisor_length && n % divisors[i] == 0) i++;
  return !(i < divisor_length);
}
