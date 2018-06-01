#include <stdio.h>
#include <math.h>


double largest_drop(double *arr, int n)
{
    if (n == 0) {
        return 0;
    }
    double highest_point = arr[0];
    double biggest_drop = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] > highest_point) {
            highest_point = arr[i];
        }
        if (arr[i] - highest_point < biggest_drop) {
            biggest_drop = arr[i] - highest_point;
        }
    }
    return (biggest_drop != 0) ? -biggest_drop : 0;
}


int main()
{
    int p, a, b, c, d, n;
    scanf("%d %d %d %d %d %d", &p, &a, &b, &c, &d, &n);
    double price_array[n];
    for (int i = 0; i < n; i++) {
        int k = i + 1;
        price_array[i] = p * (sin(a * k + b) + cos(c * k + d) + 2);
    }
    printf("%lf\n", largest_drop(price_array, n));
    return 0;
}
