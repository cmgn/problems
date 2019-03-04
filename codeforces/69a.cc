#include <bits/stdc++.h>

using namespace std;

int main(void)
{
	int n, x(0), y(0), z(0), dx, dy, dz;
	cin >> n;
	while (n--) {
		cin >> dx >> dy >> dz;
		x += dx;
		y += dy;
		z += dz;
	}
	if (x == 0 && y == 0 && z == 0) {
		cout << "YES\n";
	} else {
		cout << "NO\n";
	}
}
