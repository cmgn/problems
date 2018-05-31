#include <stdio.h>

char *days[] = {
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday"
};

int months[] = {
    31, 28, 31, 30,
    31, 30, 31, 31,
    30, 31, 30, 31
};

int main()
{
    int d, m;
    scanf("%d %d", &d, &m);
    d--;
    m--;
    while (m > 0) d += months[--m];
    printf("%s\n", days[d%7]);
    return 0;
}