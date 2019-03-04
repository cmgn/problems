#include <bits/stdc++.h>

using namespace std;
using pii = pair<int, int>;

int main(void)
{
	int s, n, a, b;
	cin >> s >> n;
	priority_queue<pii, vector<pii>, greater<pii>> h;
	for (int i = 0; i < n; i++) {
		cin >> a >> b;
		h.push({a, b});
	}
	while (!h.empty()) {
		auto [x, y] = h.top();
		h.pop();
		if (x >= s) {
			cout << "NO\n";
			return 0;
		}
		s += y;
	}
	cout << "YES\n";
}
