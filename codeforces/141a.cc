#include <bits/stdc++.h>

using namespace std;

int main(void)
{
	string s1, s2, s3;
	cin >> s1 >> s2 >> s3;
	unordered_map<char, int> cs;
	for (const auto &c : s3) {
		cs[c]++;
	}
	for (const auto &c : s1) {
		cs[c]--;
	}
	for (const auto &c : s2) {
		cs[c]--;
	}
	for (const auto &c : cs) {
		if (c.second != 0) {
			cout << "NO";
			return 0;
		}
	}
	cout << "YES";
}
