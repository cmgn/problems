#include <bits/stdc++.h>

using namespace std;

typedef long long unsigned llu;

int main(void)
{
	llu k, n, w, t(0);
	cin >> k >> n >> w;
	for (int i = 1; i <= w; i++) {
		t += k*i;
	}
	if (t <= n) {
		cout << 0 << "\n";
	} else {
		cout << t - n << "\n";
	}
}
