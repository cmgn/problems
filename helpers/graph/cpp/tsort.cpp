#include <stack>
#include <vector>

using namespace std;

// Does not support graphs that have a weight
// on their edges.
struct TopologicalSort {
    bool *s;
    stack<int> rpo;

    TopologicalSort(vector<int> g[], int n)
    {
        s = new bool[n];
        for (int v = 0; v < n; v++)
            if (!s[v]) dfs(g, v, n);
    }

    void dfs(vector<int> g[], int v, int n)
    {
        s[v] = true;
        for (const auto &u : g[v])
            if (!s[u]) dfs(g, u, n);
        rpo.push(v);
    }
};
