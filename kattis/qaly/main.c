#include <stdio.h>

int main(void)
{
	int n;
	double t, a, b;
	scanf("%d\n", &n);
	while (n--) {
		scanf("%lf %lf", &a, &b);
		t += a * b;
	}
	printf("%.03lf\n", t);
}
