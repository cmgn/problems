#include <iostream>
#include <unordered_map>
#include <sstream>

using namespace std;

int main()
{
  unordered_map<string, string> dict;
  string val, key, line;
  
  getline(cin, line);
  while (line != "") {
    stringstream ss(line);
    ss >> val >> key;
    dict[key] = val;
    getline(cin, line);
  }

  while (cin >> val) {
    if (dict.count(val) != 0) cout << dict[val] << "\n";
    else cout << "eh\n";
  }
  return 0;
}