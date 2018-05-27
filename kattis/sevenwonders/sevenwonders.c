#include <stdio.h>

#define MIN2(A, B) ((A) < (B)) ? (A) : (B)
#define MIN3(A, B, C) MIN2(MIN2(A, B), C)

int main()
{
  int t = 0, c = 0, g = 0;
  char buffer[50];
  scanf("%s", buffer);
  for (char *p = buffer; *p; p++) {
    switch(*p) {
    case 'T': t++; break;
    case 'C': c++; break;
    case 'G': g++; break;
    }
  }
  printf("%d\n", t*t + c*c + g*g + 7 * (MIN3(t, c, g)));
  return 0;
}