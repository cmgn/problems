#include <bits/stdc++.h>

using namespace std;

int main(void)
{
	int a, b, c;
	cin >> a >> b >> c;
	vector<int> res = {a+b+c, a+b*c, a*(b+c), a*b*c, a*b+c, a*b*c, (a+b)*c};
	int best = res[0];
	for (int i = 1; i < res.size(); i++) {
		best = max(res[i], best);
	}
	cout << best << "\n";
}
