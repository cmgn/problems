#include <iostream>
#include <cmath>
#include <cstdio>

#define G 9.81

using namespace std;

int main()
{
  double v0, theta, x1, h1, h2, y1, t;
  int num_tests;
  cin >> num_tests;

  for (int i = 0; i < num_tests; i++) {
    scanf("%lf %lf %lf %lf %lf", &v0, &theta, &x1, &h1, &h2);
    theta = (M_PI / 180) * theta; // convert to radians

    t = x1 / (v0 * cos(theta));
    y1 = v0 * t * sin(theta) - 0.5 * G * t * t;
    
    if (h1 + 1 <= y1 && h2 - 1 >= y1)
      cout << "Safe\n";
    else
      cout << "Not Safe\n";
  }

  return 0;
}