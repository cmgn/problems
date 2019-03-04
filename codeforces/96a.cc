#include <bits/stdc++.h>

using namespace std;

using llu = long long unsigned;
using vi = vector<int>;
using pi = pair<int, int>;

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	string s;
	cin >> s;
	int lgst = -1;
	int i = 0;
	while (i < s.size()) {
		int j = i;
		i++;
		while (i < s.size() && s[i - 1] == s[i]) {
			i++;
		}
		lgst = max(lgst, i - j);
	}
	if (lgst >= 7) {
		cout << "YES\n";
	} else {
		cout << "NO\n";
	}
	return 0;
}
