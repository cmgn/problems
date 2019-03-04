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
	cout << string(1, toupper(s[0])) << s.substr(1) << "\n";
	return 0;
}
