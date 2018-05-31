#include <bits/stdc++.h>

using namespace std;

int main()
{
    vector<function<int(int, int)>> f = {
        [](int a, int b) { return a + b; },
        [](int a, int b) { return a * b; },
        [](int a, int b) { return a - b; }
    };
    string o[] = {"+", "*", "-"};
    ostringstream e;
    set<int> a;
    int n, i, x, y, r;
    cin >> n;
    while (n--) {
        cin >> x >> y;
        for (i = 0; i < f.size() && a.count(f[i](x, y)) != 0; i++);
        if (i < f.size()) {
            r = f[i](x, y);
            e << x << " " << o[i] << " " << y << " = " << r << "\n";
            a.insert(r);
        } else {
            cout << "impossible" << "\n";
            return 0;
        }
    }
    cout << e.str() << "\n";
    return 0;
}