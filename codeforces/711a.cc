#include <bits/stdc++.h>

using namespace std;

int main(void)
{
	int n, p(-1);
	cin >> n;
	vector<string> seen(2*n);
	for (int i = 0; i < n; i++) {
		string s, l, r;
		cin >> s;
 		l = s.substr(0, 2);
 		r = s.substr(3, 2);
 		if (l[0] == 'O' && l[1] == 'O') {
 			p = 2*i;
 		} else if (r[0] == 'O' && r[1] == 'O') {
 			p = 2*i + 1;
 		}
 		seen[2*i] = l;
 		seen[2*i+1] = r;
	}
	if (p == -1) {
		cout << "NO\n";
		return 0;
	}
	cout << "YES\n";
	for (int i = 0; i < n; i++) {
		if (2*i == p) {
			cout << "++";
		} else {
			cout << seen[2*i];
		}
		cout << "|";
		if (2*i + 1 == p) {
			cout << "++";
		} else {
			cout << seen[2*i+1];
		}
		cout << "\n";
	}
}
