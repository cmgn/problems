#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

typedef pair<int, int> pii;
typedef vector<pii> vii;

int main()
{
    int n, l, u, r;
    vii ms;
    cin >> n;
    while (n--) {
        cin >> l >> u;
        ms.push_back(pii(l, u));
    }
    sort(ms.begin(), ms.end(), [](pii &a, pii &b) {
        return (a.second == b.second) ? a.first < b.first : a.second < b.second;
    });
    r = 1;
    l = ms[0].second;
    for (int i = 1; i < ms.size(); i++) {
        if (ms[i].first > l) {
            l = ms[i].second;
            r++;
        }
    }
    cout << r << "\n";
    return 0;
}