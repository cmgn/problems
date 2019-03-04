#include <bits/stdc++.h>

using namespace std;

using llu = long long unsigned;
using vi = vector<int>;
using pi = pair<int, int>;

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n, exits, enters, p(0), t(0);
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> exits >> enters;
		p -= exits;
		p += enters;
		t = max(t, p);
	}
	cout << t << "\n";
	return 0;
}
