#include <bits/stdc++.h>

using namespace std;

int main(void) {
    queue<int> ord;
    map<int, int> freq;
    int n;
    while (cin >> n) {
        if (freq.find(n) == freq.end()) {
            ord.emplace(n);
            freq[n] = 0;
        }
        freq[n]++;
    }
    while (!ord.empty()) {
        n = ord.front();
        ord.pop();
        cout << n << " " << freq[n] << "\n";
    }
}