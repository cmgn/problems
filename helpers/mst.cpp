#include <vector>
#include <queue>
#include <functional>
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
        return {total_cost, es};
    }
};

int main()
{
    auto m = MinimumSpanningTree();
    m.initialise(4);
    m.add_edge(0, 1, 2);
    m.add_edge(1, 3, 7);
    m.add_edge(3, 2, 8);
    m.add_edge(2, 0, 5);
    m.add_edge(0, 3, 3);
    m.add_edge(2, 1, 1);
    auto r = m.compute_mst();
    cout << r.cost << "\n";
    sort(r.edges.begin(), r.edges.end());
    for (const auto &e : r.edges)
        cout << e.first << " " << e.second << "\n";
    return 0;
}