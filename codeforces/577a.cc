#include <bits/stdc++.h>

using namespace std;

int main(void)
{
	int n, x, t(0);
	cin >> n >> x;
	for (int i = 1; i <= n; i++) {
		if (x % i == 0 and x / i <= n) {
			t++;
		}
	}
	cout << t << "\n";
}
