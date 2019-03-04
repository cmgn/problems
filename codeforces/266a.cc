#include <bits/stdc++.h>

using namespace std;

using llu = long long unsigned;
using vi = vector<int>;
using pi = pair<int, int>;

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n, j(0), i(0), t(0);
	string s;
	cin >> n >> s;
	while (i < n) {
		j = i;
		i++;
		while (i < n && s[i - 1] == s[i]) {
			i++;
		}
		t += i - j - 1;
	}
	cout << t << "\n";
	return 0;
}
