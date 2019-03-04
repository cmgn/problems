#include <bits/stdc++.h>

using namespace std;

int main(void)
{
	int n, m, odd(0), even(0), lodd(0), leven(0);
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> m;
		if (m % 2 == 0) {
			even++;
			leven = i;
		} else {
			odd++;
			lodd = i;
		}
	}
	if (odd > even) {
		cout << leven + 1;
	} else {
		cout << lodd + 1;
	}
}
