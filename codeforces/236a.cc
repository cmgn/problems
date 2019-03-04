#include <bits/stdc++.h>

using namespace std;

int main(void)
{
	unordered_set<char> cs;
	string s;
	cin >> s;
	for (const auto &c : s) {
		cs.insert(c);
	}
	if (cs.size() % 2) {
		cout << "IGNORE HIM!\n";
	} else {
		cout << "CHAT WITH HER!\n";
	}
}
