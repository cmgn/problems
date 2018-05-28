#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;

int main()
{
  unordered_map<string, vector<int>> d;
  int n, y;
  string p;
  cin >> n;
  while (n--) {
    cin >> p >> y;
    d[p].push_back(y);
  }
  for (unordered_map<string, vector<int>>::iterator k = d.begin(); k != d.end(); k++)
    sort((*k).second.begin(), (*k).second.end());
  cin >> n;
  while (n--) {
    cin >> p >> y;
    cout << d[p][y-1] << "\n";
  }
  return 0;
}