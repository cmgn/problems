#include <bits/stdc++.h>

using namespace std;

int main(void)
{
	int n, t;
	string s;
	cin >> n >> t >> s;
	while (t--) {
		for (int i = 0; i < s.size(); i++) {
			if (s[i] == 'B' && i + 1 < s.size() && s[i+1] == 'G') {
				s[i] = 'G';
				s[i+1] = 'B';
				i++;
			}
		}
	}
	cout << s << "\n";
}
