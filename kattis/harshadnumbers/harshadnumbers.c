#include <stdio.h>

int sumdigits(int n)
{
	int t = 0;
	while (n > 0) {
		t += n % 10;
		n /= 10;
	}
	return t;
}

int main(void)
{
	int n;
	scanf("%d", &n);
	while (n % sumdigits(n)) {
		n++;
	}
	printf("%d\n", n);
	return 0;
}

