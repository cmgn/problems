#include <iostream>

using namespace std;

int main()
{
  int n;
  while (cin >> n) 
    cout << ((n == 1) ? 1 : (n - 1) * 2) << "\n";
  return 0;
}