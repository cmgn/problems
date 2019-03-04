#include <bits/stdc++.h>

using namespace std;

int main(void)
{
	int n, a, t(0);
	cin >> n;
	vector<int> c(n);
	for (int i = 0; i < n; i++) {
		cin >> c[i];
		t += c[i];
	}
	sort(c.rbegin(), c.rend());
	int i(0), s(0);
	while (i < c.size() && t / 2 >= s) {
		s += c[i];
		i++;
	}
	cout << i << "\n";
}
