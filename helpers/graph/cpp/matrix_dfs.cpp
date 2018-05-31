#include <algorithm>
#include <stack>
#include <set>

using namespace std;

int bfs(int **adj_matr, int n, int u)
{
    int v;
    stack<int> _s;
    set<int> s;
    _s.push(u);
    while (!_s.empty()) {
        v = _s.top();
        if (v == u) return v;
        for (int i = 0; i < n; i++) {
            if (adj_matr[v][i] != 0 && !s.count(i)) {
                _s.push(i);
                s.insert(i);
            }
        }
        _s.pop();
    }
    return -1;
}
