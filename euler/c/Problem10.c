// The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
// Find the sum of all the primes below two million.

#include <stdio.h>
#include <math.h>

typedef unsigned long long int llu;

int is_prime(llu n);

int main(int argc, char **argv)
{
  llu total = 2;
  for (llu i = 3; i < 2000000; i += 2)
    total += i * is_prime(i);
  printf("%llu", total);
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
