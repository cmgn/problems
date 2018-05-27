#include <iostream>
#include <algorithm>

using namespace std;

int main(int argc, char **argv)
{
  string order;
  int numbers[3];
  cin >> numbers[0] >> numbers[1] >> numbers[2] >> order;
  sort(numbers, numbers + 3);
  for (int i = 0; i < 3; i++)
    cout << numbers[order[i] - 'A'] << ' ';
  return 0;
}