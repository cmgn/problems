#include <cmath>
#include <iostream>
#include <map>
#include <string>
#include <utility>

using pmap = std::map<int, int>;
using pfacr = std::tuple<bool, pmap>;

pfacr
pfac(int n)
{
  bool neg = (n < 0);
  n = abs(n);
  pmap factors;
  while (n % 2 == 0) {
    if (factors.count(2) == 0) {
      factors[2] = 0;
    }
    factors[2]++;
    n /= 2;
  }
  int m = (int)(sqrt(n) + 1);
  for (int i = 2; i < m; i++) {
    while (n % i == 0) {
      if (factors.count(i) == 0) {
        factors[i] = 0;
      }
      factors[i]++;
      n /= i;
    }
  }
  if (n > 2) {
    factors[n] = 1;
  }
  return { neg, factors };
}

int
main(void)
{
  std::string line;
  while (std::getline(std::cin, line)) {
    auto [neg, facs] = pfac(std::stoi(line));
    if (neg) {
      std::cout << -1 << " ";
    }
    for (const auto& x : facs) {
      auto [y, z] = x;
      if (z > 1) {
        std::cout << y << "^" << z << " ";
      } else {
        std::cout << y << " ";
      }
    }
    std::cout << "\n";
  }
}