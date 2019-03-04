#include <bits/stdc++.h>

using namespace std;

int main(void)
{
	int a, b;
	cin >> a >> b;
	int c = min(a, b);
	a -= c;
	b -= c;
	cout << c << " " << max(a, b) / 2 << "\n";
}
