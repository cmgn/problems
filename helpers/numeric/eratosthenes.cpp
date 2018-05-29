#include <vector>
#include <cmath>

using namespace std;

vector<bool> prime_sieve(int n)
{
    vector<bool> v(n);
    fill(v.begin(), v.end(), true);
    v[0] = false; v[1] = false;
    int m = (int) sqrt(n) + 1;
    for (int i = 2; i < m; i++) {
        if (v[i]) for (int j = i*i; j < n; j += i) v[j] = false;
    }
    return v;
}