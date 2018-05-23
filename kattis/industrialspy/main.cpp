#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>
#include <set>
#include <map>

bool is_prime(int n) 
{
  if (n == 2 || n == 3) {
    return true;
  } else if (n == 1 || n % 2 == 0) {
    return false;
  } else {
    int up_to = (int) sqrt((double) n) + 1;
    for (int i = 3; i < up_to; i += 2) {
      if (n % i == 0) 
        return false;
    }
    return true;
  }
}

int main()
{
  std::ios_base::sync_with_stdio(false);
  std::map<int, bool> prime_cache;

  unsigned int m;
  std::cin >> m;
  
  for (int i = 0; i < m; i++) {
    std::string str;
    std::cin >> str;

    std::set<int> seen;
    std::sort(str.begin(), str.end());

    do {
      for (int i = 1; i <= str.size(); i++) {
        int num = std::stoi(str.substr(0, i));
        if (prime_cache.count(num) != 0 and prime_cache[num]) {
          seen.insert(num);
        } else {
          prime_cache[num] = is_prime(num);
          if (prime_cache[num]) {
            seen.insert(num);
          }
        }
      }
    } while (std::next_permutation(str.begin(), str.end()));
    
    std::cout << seen.size() << '\n';
  }
}
