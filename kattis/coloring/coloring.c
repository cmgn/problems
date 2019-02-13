#include <string.h>
#include <stdio.h>

int n;
int g[12][12];
int c[12];

void findsafe(int *s, int u)
{
	for (int v = 0; v < n; v++) {
		if (g[u][v] && c[v] != -1) {
			s[c[v]] = 0;
		}
	}
}

int trycolor(int maxc, int u)
{
	if (u >= n) {
		return 1;
	}
	int safe[12];
	for (int i = 0; i < 12; i++) {
		safe[i] = 1;
	}
	findsafe(safe, u);
	for (int col = 0; col < maxc; col++) {
		if (!safe[col]) {
			continue;
		}
		c[u] = col;
		if (trycolor(maxc, u + 1)) {
			return 1;
		}
	}
	c[u] = -1;
	return 0;
}

int main(void)
{
	scanf("%d\n", &n);
	memset(g, 0, 12*12*sizeof(int));
	for (int i = 0; i < n; i++) {
		int prv = 0;
		for (;;) {
			char chr = getc_unlocked(stdin);
			if (!chr || chr == ' ' || chr == '\n') {
				g[i][prv] = 1;
				prv = 0;
				if (chr != ' ') {
					break;
				}
				continue;
			}
			prv = prv * 10 + chr - '0';
		}
	}
	for (int i = 0; i < 12; i++) {
		c[i] = -1;
	}
	for (int i = 2; ; i++) {
		if (trycolor(i, 0)) {
			printf("%d\n", i);
			break;
		}
	}
	return 0;
}
