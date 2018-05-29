#include <vector>
#include <iostream>
#include <cmath>

using namespace std;

vector<bool> prime_sieve(int n)
{
    int c = n;
    vector<bool> v(n);
    fill(v.begin(), v.end(), true);
    v[0] = false;
    v[1] = false;
    int m = (int) sqrt(n) + 1;
    for (int i = 2; i < m; i++) {
        if (v[i])
            for (int j = i*i; j < n; j += i) {
                if (v[j]) {c--;}
                v[j] = false;   
            }
    }
    cout << c - 2 << "\n";
    return v;
}

int main()
{
    int n, q;
    cin >> n >> q;
    auto v = prime_sieve(n + 1);
    while (q--) {
        cin >> n;
        cout << v[n] << "\n";
    }
    return 0;
}