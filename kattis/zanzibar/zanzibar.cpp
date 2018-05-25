#include <iostream>


using namespace std;


int main()
{
  ios_base::sync_with_stdio(false);
  int number_of_tests;
  cin >> number_of_tests;

  for (int test_no = 0; test_no < number_of_tests; test_no++) {
    int foreign = 0;
    int previous_population, current_population, population_diff;
    
    cin >> previous_population;
    cin >> current_population;
    
    while (current_population) {
      population_diff = current_population - (previous_population * 2);
      if (population_diff > 0) 
        foreign += population_diff;
      previous_population = current_population;
      cin >> current_population;
    }

    cout << foreign << "\n";
  }

  return 0;
}