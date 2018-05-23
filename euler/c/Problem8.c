#include <stdio.h>

typedef unsigned long long int llu;

static unsigned int nums[] = {
#include "input/Problem8_input.txt"
};

llu product(llu i, llu j)
{
  llu total = 1;
  for (i = i; i < j; i++) total *= nums[i];
  return total;
}

int main()
{
  llu max = 0, curr_product = 0;
  for (int i = 0; i < 988; i++) {
    curr_product = product(i, i + 13);
    max = (max > curr_product) ? max : curr_product;
  }
  printf("%llu\n", max);
  return 0;
}