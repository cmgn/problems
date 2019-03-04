#include <bits/stdc++.h>

using namespace std;

int main(void)
{
	long long unsigned n, m, a, b, s1, s2;
	cin >> n;
	while (n--) {
		cin >> m >> a >> b;
		s1 = (m / 2) * b + (m % 2) * a;
		s2 = m * a;
		cout << min(s1, s2) << "\n";
	}
}
