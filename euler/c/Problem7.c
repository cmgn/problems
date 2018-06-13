#include <stdio.h>
#include <math.h>

/*
 * What is the 10001st prime number?
 */

typedef long long unsigned int llu;

int is_prime(llu n);
llu prime_generator();

int main()
{
  for (int i = 0; i < 10000; i++) prime_generator();
  printf("%llu\n", prime_generator());
  return 0;
}

int is_prime(llu n) 
{
  if (n == 2 || n == 3) {
    return 1;
  } else if (n == 1 || n % 2 == 0) {
    return 0;
  } else {
    llu up_to = (llu) sqrt((double) n) + 1;
    for (int i = 3; i < up_to; i += 2) {
      if (n % i == 0) 
        return 0;
    }
    return 1;
  }
}

llu prime_generator()
{
  static llu n = 1;
  while (!is_prime((n += 2)));
  return n;
}