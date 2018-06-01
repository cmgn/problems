#include <iostream>
#include <unordered_set>

using namespace std;

int main()
{
    unordered_set<string> parts;
    string part;
    int number_of_parts, number_of_days, replaced = 0;
    cin >> number_of_parts >> number_of_days;
    for (int day = 0; day < number_of_days; day++) {
        cin >> part;
        if (parts.count(part) == 0) {
            replaced++;
            if (replaced == number_of_parts) {
                cout << day + 1 << "\n";
            }
        }
        parts.insert(part);
    }
    if (replaced < number_of_parts) {
        cout << "paradox avoided\n";
    }
    return 0;
}
