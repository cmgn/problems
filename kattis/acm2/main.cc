#include <bits/stdc++.h>

using namespace std;

int main(void)
{
	int i = 0, n = 0, p = 0, t = 0, pt = 0;
	cin.sync_with_stdio(false);
	cin >> n >> p;
	vector<int> v(n);
	for (i = 0; i < n; i++) {
		cin >> v[i];
	}
	t = v[p];
	v[p] = v[0];
	v[0] = t;
	t = 0;
	sort(v.begin() + 1, v.end());
	for (i = 0; i < n && t + v[i] <= 300; i++) {
		t += v[i];
		pt += t;
	}
	cout << i << " " << pt << "\n";
	return 0;
}
