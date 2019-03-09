#include <bits/stdc++.h>

using namespace std;

map<string, int> M;

void genpos() {
    queue<string> q;
    for (char c = 'a'; c <= 'z'; c++) {
        q.emplace(string(1, c));
    }
    int count = 1;
    while (!q.empty()) {
        string word = q.front();
        q.pop();
        M[word] = count++;
        if (word.size() > 5) {
            continue;
        }
        for (char c = 'a'; c <= 'z'; c++) {
            if (c > word[word.size() - 1]) {
                q.emplace(word + c);
            }
        }
    }
}

int main(void) {
    genpos();
    string word;
    while (cin >> word) {
        if (M.find(word) != M.end()) {
            cout << M[word] << "\n";
        } else {
            cout << 0 << "\n";
        }
    }
    return 0;
}