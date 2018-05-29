#include <vector>
#include <queue>
#include <functional>
#include <sstream>
#include <string>
#include <algorithm>
#include <iostream>
#include <utility>

using namespace std;

typedef pair<int, int> pii;
typedef pair<int, pii> edge;

typedef struct {
    int cost;
    vector<pii> edges;
} mst_return_type;

struct UnionFind {
    int p[20001];
    int size = 0;
    int c;

    void initialise(int n) 
    {
        for (int i = 1; i < n + 1; i++) p[i] = i;
        size = n;
    }

    void _union(int a, int b)
    {
        a = find(a);
        b = find(b);
        if (a == b) return;
        if (b < a) {
            c = b;
            b = a;
            a = c;
        }
        p[b] = a;
        size--;
    }

    int find(int a) 
    {
        while (a != p[a]) { p[a] = p[p[a]]; a = p[a]; }
        return a;
    }
};

struct MinimumSpanningTree {
    int num_vert;
    priority_queue<edge, vector<edge>, greater<edge>> edges;
    
    void initialise(int n)
    {
        num_vert = n;
    }

    void add_edge(int src, int dst, int cost)
    {
        edges.push(edge(cost, pii(src, dst)));
        edges.push(edge(cost, pii(dst, src)));
    }

    mst_return_type compute_mst()
    {
        UnionFind uf;
        vector<pii> es;
        int total_cost = 0, cost, src, dst;
        uf.initialise(num_vert);
        while (uf.size != 1 && !edges.empty()) {
            edge e = edges.top();
            cost = e.first, src = e.second.first, dst = e.second.second;
            if (uf.find(src) != uf.find(dst)) {
                uf._union(src, dst);
                total_cost += cost;
                es.push_back(e.second);
            }
            edges.pop();
        }
        if (uf.size != 1) total_cost = -1;
        return {total_cost, es};
    }
};

int main()
{
    mst_return_type r;
    int n, m, u, v, w;
    cin >> n >> m;
    while (n || m) {
        MinimumSpanningTree mst;
        mst.initialise(n);
        while (m--) {
            cin >> u >> v >> w;
            mst.add_edge(u, v, w);
        }
        r = mst.compute_mst();
        if (r.cost == -1)
            cout << "Impossible\n";
        else {
            cout << r.cost << "\n";
            sort(r.edges.begin(), r.edges.end());
            for (const auto &e : r.edges)
                cout << e.first << " " << e.second << "\n";
        }
        cin >> n >> m;
    }
    return 0;
}
