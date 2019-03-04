#include <bits/stdc++.h>

using namespace std;

int main() {
	bool active = false;
	for (;;) {
		char c = getchar();
		switch (c) {
		case EOF:
			return 0;
		case '"':
			if (!active) {
				printf("``");
			} else {
				printf("''");
			}
			active = !active;
			break;
		default:
			printf("%c", c);
		}
	}
}
