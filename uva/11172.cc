#include <bits/stdc++.h>

using namespace std;

int main() {
	int n, a, b;
	scanf("%d", &n);
	while (n--) {
		scanf("%d %d", &a, &b);
		if (a == b) {
			puts("=");
		} else if (a < b) {
			puts("<");
		} else {
			puts(">");
		}
	}
}
