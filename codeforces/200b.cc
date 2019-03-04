#include <bits/stdc++.h>

using namespace std;

int main(void)
{
	int n, s, t(0);
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> s;
		t += s;
	}
	cout << (double) t / n << "\n";
}
