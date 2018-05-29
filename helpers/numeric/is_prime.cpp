#include <cmath>
#include <unordered_map>
using namespace std;


unordered_map<int> prime_cache;


bool is_prime(int n)
{
    if (prime_cache.count(n))
        return prime_cache[n];
    prime_cache[n] = _is_prime(n);
    return prime_cache[n];
}


bool _is_prime(int n) 
{
    if (n < 2) return false;
    else if (n < 4) return true;
    else if (n % 2 == 0 || n % 3 == 0) return false;
    else if (n < 25) return true;
    for (int i = 5; i*i <= n; i += 6)
        if (n % i == 0 || n % (i + 2) == 0) return false;
    return true;
}
