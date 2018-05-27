#include <stdio.h>

int cups[3] = {1, 0, 0};

void swap(int i, int j)
{
  int temp = cups[i];
  cups[i] = cups[j];
  cups[j] = temp;
}

int main()
{
  char buffer[50];
  scanf("%s", buffer);
  
  for (char *p = buffer; *p; p++) {
    switch (*p) {
    case 'A': swap(0, 1); break;
    case 'B': swap(1, 2); break;
    case 'C': swap(0, 2); break;
    }
  }

  for (int i = 0; i < 3; i++)
    if (cups[i]) printf("%d\n", i + 1);
  return 0;
}
