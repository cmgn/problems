#include <bits/stdc++.h>

int main()
{
  int n, k;
  std::cin >> n >> k;
  std::vector<std::pair<long long, int>> a, d, h;
  for (int i = 0; i < n; i++) {
    long long aa, dd, hh;
    std::cin >> aa >> dd >> hh;
    a.push_back({aa, i});
    d.push_back({dd, i});
    h.push_back({hh, i});
  }
  std::sort(a.rbegin(), a.rend());
  std::sort(d.rbegin(), d.rend());
  std::sort(h.rbegin(), h.rend());
  std::set<int> s;
  for (int i = 0; i < k; i++) {
    s.insert(a[i].second);
    s.insert(d[i].second);
    s.insert(h[i].second);
  }
  std::cout << s.size() << "\n";
}