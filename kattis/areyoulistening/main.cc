#include <bits/stdc++.h>

int main(void)
{
	int cx, cy, n, x, y, r;
	std::cin.sync_with_stdio(false);
	std::cin >> cx >> cy >> n;
	// A better way of doing this is to use a priority queue, but this is good enough.
	// An even *better* way is to just declare 3 double variables and do something like
	// if (curr < d0) {
	//   d2 = d1;
	//   d1 = d0;
	//   d0 = curr;
	// } else if (curr < d1) {
	//   d2 = d1;
	//   d1 = curr;
	// } ...
	// which operates in constant time.
	std::vector<double> v(n);
	for (int i = 0; i < n; i++) {
		std::cin >> x >> y >> r;
		v[i] = std::sqrt((x-cx)*(x-cx) + (y-cy)*(y-cy)) - r;
	}
	std::sort(v.begin(), v.end());
	if (v[2] < 0) {
		v[2] = 0;
	}
	std::cout << (int) v[2] << "\n";
}

