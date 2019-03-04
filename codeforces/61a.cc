#include <bits/stdc++.h>

using namespace std;

int main(void)
{
	string a, b;
	cin >> a >> b;
	for (int i = 0; i < a.size(); i++) {
		a[i] -= '0';
		b[i] -= '0';
		if (a[i] ^ b[i]) {
			cout << "1";
		} else {
			cout << "0";
		}
	}
	cout << "\n";
}
