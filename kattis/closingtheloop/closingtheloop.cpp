#include <string>
#include <iostream>
#include <algorithm>
#include <vector>

// Overkill but I wanted to do some stuff with heaps

typedef enum {
  RED,
  BLUE
} colour;


int main()
{
  int test_cases;
  std::cin >> test_cases;
  
  for (int test_no = 0; test_no < test_cases; test_no++) {
    std::vector<int> reds;
    std::vector<int> blues;
    std::string input;

    int num_pieces;
    std::cin >> num_pieces;

    for (int i = 0; i < num_pieces; i++) {
      std::cin >> input;
      if (input[input.size() - 1] == 'R')
        reds.push_back(std::stoi(input.substr(0, input.size() - 1)) - 1);
      else
        blues.push_back(std::stoi(input.substr(0, input.size() - 1)) - 1);
    }

    std::make_heap(reds.begin(), reds.end());
    std::make_heap(blues.begin(), blues.end());

    colour state = reds.size() > blues.size() ? RED : BLUE;
    int size = 0;

    while ((!reds.empty() && state == BLUE) || (!blues.empty() && state == RED)) {
      // pointer fun
      std::vector<int> *active = (state == BLUE) ? &reds : &blues;
      size += (*active)[0];
      std::pop_heap((*active).begin(), (*active).end());
      (*active).pop_back();
      state = (state == RED) ? BLUE : RED;
    }

    std::cout << "Case #" << test_no + 1 << ": " <<size << "\n";
  }
}