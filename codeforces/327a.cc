#include <bits/stdc++.h>

using namespace std;

int main(void)
{
	int n;
	cin >> n;
	vector<int> v(n);
	for (int i = 0; i < n; i++) {
		cin >> v[i];
	}
	int m = 0;
	for (int i = 0; i < n; i++) {
		for (int j = i; j < n; j++) {
			int t = 0;
			for (int k = 0; k < n; k++) {
				if (k < i || k > j) {
					t += v[k];
				} else {
					t += 1 - v[k];
				}
			}
			m = max(m, t);
		}
	}
	cout << m << "\n";
}
