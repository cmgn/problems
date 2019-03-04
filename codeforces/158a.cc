#include <bits/stdc++.h>

using namespace std;

int main(void) {
	int n, k;
	cin >> n >> k;
	k--;
	vector<int> s(n);
	for (int i = 0; i < n; i++) {
		cin >> s[i];
	}
	int m = max(1, s[k]);
	int i = 0;
	while (i < s.size() && s[i] >= m) {
		i++;
	}
	cout << i << "\n";
}
