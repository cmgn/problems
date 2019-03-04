#include <bits/stdc++.h>

using namespace std;

int main(void)
{
	int a;
	unordered_set<int> c;
	for (int i = 0; i < 4; i++) {
		cin >> a;
		c.insert(a);
	}
	cout << 4 - c.size() << "\n";
}
