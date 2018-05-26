#include <iostream>
#include <map>
#include <unordered_map>

using namespace std;

int main()
{
  uint highest_no = 0;
  uint highest_count = 0;
  uint counter = 0;
  unordered_map<int, int> cache;
  
  for (int n = 0; n < 1000000; n++) {
    counter = 1;
    
    unsigned int m = n;
    while (m > 1 && cache.count(m) == 0) {
      m = (m & 1) ? (3 * m + 1) : m >> 1;
      counter++;
    }

    if (m > 1) counter += cache[m];
    
    cache[n] = counter;
    if (counter > highest_count) {
      highest_count = counter;
      highest_no = n;
    }
  }
  
  cout << highest_no << "\n";
}