#include <bits/stdc++.h>

int main(void)
{
	std::cin.sync_with_stdio(false);
	
	int n, x;
	std::cin >> n >> x;
	
	std::vector<int> vect(n);
	
	for (int i = 0; i < n; i++) {
		std::cin >> vect[i];
	}

	std::sort(vect.begin(), vect.end());

	int i;
	
	for (i = 1; i < n && vect[i] + vect[i - 1] <= x; i++) {

	}

	std::cout << i << "\n";
}
