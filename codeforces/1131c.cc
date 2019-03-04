#include <bits/stdc++.h>

using namespace std;

int main(void)
{
	int n;
	cin >> n;
	vector<int> vs(n);
	while (n--) {
		cin >> vs[n];
	}
	sort(vs.begin(), vs.end());
	for (int i = 0; i < vs.size(); i += 2) {
		cout << vs[i] << " ";
	}
	int m = vs.size() - 1;
	m -= vs.size() % 2;
	for (int i = m; i >= 0; i -= 2) {
		cout << vs[i] << " ";
	}
	cout << "\n";
}
