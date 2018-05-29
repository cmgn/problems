#include <cmath>
#include <set>

using namespace std;

set<int> prime_factors(int n)
{
    set<int> s;
    int m = 2;
    while (m * m < n) {
        if (n % m == 0) {
            s.insert(z);
            n /= 2;
        } else {
            m++;
        }
    }
    return s;
}