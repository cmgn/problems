#include <bits/stdc++.h>

using namespace std;

int main(void)
{
	string s;
	int n, x = 0;
	cin >> n;
	while (n--) {
		cin >> s;
		if (s[0] == '+' || s[2] == '+') {
			x++;
		} else {
			x--;
		}
	}
	cout << x << "\n";
}
