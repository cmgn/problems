#include <bits/stdc++.h>

#define MAX_SIZE 200001

using namespace std;

int fast_get_int()
{
    int c = getc_unlocked(stdin);
    int r = 0;
    while (c >= 48 && c <= 57) {
        r = r * 10 + c - 48;
        c = getc_unlocked(stdin);
    }
    return r;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int C = fast_get_int(), P = fast_get_int(), X = fast_get_int(), L = fast_get_int(), u, v;
    
    vector<int> graph[MAX_SIZE];
    int starting_neighbours[MAX_SIZE];
    int neighbours_now[MAX_SIZE];
    bool left[MAX_SIZE];
    
    while (P--) {
        u = fast_get_int(), v = fast_get_int();
        starting_neighbours[u]++;
        starting_neighbours[v]++;
        neighbours_now[u]++;
        neighbours_now[v]++;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    queue<int> leaving;
    leaving.push(L);
    left[L] = true;
    while (!leaving.empty()) {
        u = leaving.front();
        leaving.pop();
        for (int v : graph[u]) {
            if (left[v]) {
                continue;
            }
            neighbours_now[v]--;
            if (2 * neighbours_now[v] <= starting_neighbours[v]) {
                left[v] = true;
                leaving.push(v);
            }
        }
    }
    
    if (left[X]) {
        printf("leave");
    } else {
        printf("stay");
    }
}
