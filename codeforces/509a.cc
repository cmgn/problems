#include <bits/stdc++.h>

using namespace std;

int main(void)
{
	int m(1), n;
	cin >> n;
	vector<int> t(n*n);
	for (int i = 0; i < n; i++) {
		t[i] = 1;
		t[i*n] = 1;
	}
	for (int i = 1; i < n; i++) {
		for (int j = 1; j < n; j++) {
			t[i*n+j] = t[(i-1)*n+j] + t[i*n+j-1];
			m = max(t[i*n+j], m);
		}
	}
	cout << m << "\n";
}
