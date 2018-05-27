#include <iostream>
#include <cmath>

using namespace std;

int main()
{
  int n, i, m, p, x = 0;
  string s;
  cin >> n;
  for (i = 0; i < n; i++) {
    cin >> s;
    m = stoi(s.substr(0, s.size() - 1));
    p = s[s.size() - 1] - '0';
    x += pow(m, p);
  }
  cout << x << "\n";
}