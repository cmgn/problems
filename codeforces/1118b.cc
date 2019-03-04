#include <bits/stdc++.h>

using namespace std;

typedef long long unsigned llu;

int main(void)
{
	llu n;
	cin >> n;
	vector<llu> candies(n);

	int oddSuffix = 0, evenSuffix = 0, evenPrefix = 0, oddPrefix = 0;

	for (int i = 0; i < n; i++) {
		cin >> candies[i];
		if (i & 1) {
			evenSuffix += candies[i];
		} else {
			oddSuffix += candies[i];
		}
	}
	
	int ans = 0;
	for (int i = 0; i < n; i++) {
		if (i & 1) {
			evenSuffix -= candies[i];
		} else {
			oddSuffix -= candies[i];
		}
		if (evenPrefix + oddSuffix == oddPrefix + evenSuffix) {
			ans++;
		}
		if (i & 1) {
			evenPrefix += candies[i];
		} else {
			oddPrefix += candies[i];
		}
	}
	cout << ans << "\n";
}
