#include <algorithm>
#include <queue>
#include <set>

using namespace std;

int bfs(int **adj_matr, int n, int u)
{
    int v;
    queue<int> q;
    set<int> s;
    q.push(u);
    while (!q.empty()) {
        v = q.front();
        if (v == u) return v;
        for (int i = 0; i < n; i++) {
            if (adj_matr[v][i] != 0 && !s.count(i)) {
                q.push(i);
                s.insert(i);
            }
        }
        q.pop();
    }
    return -1;
}
