#include <bits/stdc++.h>

using namespace std;

bool is_vowel(char c)
{
	static char *vowels = "aeiouyYAEIOU";
	for (char *p = vowels; *p; p++) {
		if (*p == c) {
			return true;
		}
	}
	return false;
}

int main(void)
{
	string s;
	cin >> s;
	for (int i = 0; i < s.size(); i++) {
		if (!is_vowel(s[i])) {
			cout << '.' << string(1, tolower(s[i]));
		}
	}
}
