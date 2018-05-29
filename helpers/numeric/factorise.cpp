#include <cmath>
#include <set>

using namespace std;

set<int> factorise(int n)
{
    set<int> v;
    for (int i = 1; i*i < n; i++) {
        if (n % i == 0) { 
            v.insert(i);
            v.insert(n/i);
        }
    }
    // v.erase(n);
    return v;
}
