#include <bits/stdc++.h>

using namespace std;

int main(void)
{
	int n, m, o(0), u(0);
	cin >> n;
	while (n--) {
		cin >> m;
		if (m == -1) {
			if (o > 0) {
				o--;
			} else {
				u++;
			}
		} else {
			o += m;
		}
	}
	cout << u << "\n";
}
