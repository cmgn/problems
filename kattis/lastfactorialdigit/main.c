#include <stdio.h>

int last[] = {1, 1, 2, 6, 4, 0, 0, 0, 0, 0, 0};

int main(void)
{
	int n, m;
	scanf("%d", &n);
	while (n--) {
		scanf("%d", &m);
		printf("%c\n", last[m] + '0');
	}
}
