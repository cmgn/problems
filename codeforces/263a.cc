#include <bits/stdc++.h>

using namespace std;

using llu = long long unsigned;
using vi = vector<int>;
using pi = pair<int, int>;

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n;
	for (int i = 0; i < 25; i++) {
		cin >> n;
		if (n == 0) {
			continue;
		}
		int r = i / 5, c = i % 5;
		cout << abs(r - 2) + abs(c - 2) << "\n";
		break;
	}
	return 0;
}
