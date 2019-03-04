#include <bits/stdc++.h>

using namespace std;

int gcd(int a, int b)
{
	int c;
	while (b != 0) {
		c = b;
		b = a % b;
		a = c;
	}
	return a;
}

int main(void)
{
	int k(0), a, b, c, n;
	cin >> a >> b >> n;
	while (n >= 0) {
		k++;
		n -= gcd((k & 1) ? a : b, n);
	}
	cout << (k & 1) << "\n";
}
