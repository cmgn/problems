#include <stdio.h>

int main(void)
{
	int n;
	scanf("%d", &n);
	if (n <= 2) {
		printf("%d\n", 1);
	} else {
		printf("%d\n", n - 2);
	}
}
