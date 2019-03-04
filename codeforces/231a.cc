#include <bits/stdc++.h>

using namespace std;

int main(void)
{
	int n, a, b, c, t = 0;
	cin >> n;
	while (n--) {
		int a, b, c;
		cin >> a >> b >> c;
		if (a + b + c > 1) {
			t++;
		}
	}
	cout << t << "\n";
}
