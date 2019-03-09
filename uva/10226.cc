#include <bits/stdc++.h>

using namespace std;

int main(void) {
    int n;
    scanf("%d", &n);
    getchar();
    getchar();
    while (n--) {
        map<string, int> freq;
        int total = 0;
        string tree;
        while (getline(cin, tree)) {
            if (tree.compare("") == 0) {
                break;
            }
            freq[tree]++;
            total++;
        }
        if (total < 0) {
            total++;
        }
        for (const auto &x : freq) {
            printf("%s %.4f\n", x.first.c_str(), 100 * (double) x.second / total);
        }
        if (n) {
            putchar('\n');
        }
    }
}