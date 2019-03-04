#include <bits/stdc++.h>

using namespace std;

using llu = long long unsigned;
using vi = vector<int>;
using pi = pair<int, int>;

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	string a, b;
	cin >> a >> b;
	int cmp = 0;
	for (int i = 0; i < a.size(); i++) {
		if (toupper(a[i]) > toupper(b[i])) {
			cmp = 1;
			break;
		} else if (toupper(a[i]) < toupper(b[i])) {
			cmp = -1;
			break;
		}
	}
	cout << cmp << "\n";
	return 0;
}
