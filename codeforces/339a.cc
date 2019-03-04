#include <bits/stdc++.h>

using namespace std;

int main(void)
{
	string s;
	cin >> s;
	vector<int> v(s.size()/2 + 1);
	for (int i = 0; i < s.size(); i += 2) {
		v[i/2] = s[i] - '0';
	}
	sort(v.begin(), v.end());
	for (int i = 0; i < v.size(); i++) {
		cout << v[i];
		if (i != v.size() - 1) {
			cout << "+";
		}
	}
	cout << "\n";
}
