#include <iostream>
#include <vector>

using namespace std;

int main()
{
  int number_of_tasks, time_left, current_task, i = 0;
  cin >> number_of_tasks >> time_left >> current_task;
  
  while (time_left >= current_task && ++i < number_of_tasks) {
    time_left -= current_task;
    cin >> current_task;
  }

  cout << i;
  return 0;
}
