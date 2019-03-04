#include <bits/stdc++.h>

using namespace std;

class UnionFind {
private:
    vector<int> parent, size;
    int n;

public:
    UnionFind(int n_) {
        n = n_;
        parent = vector<int>(n), size = vector<int>(n);
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
    }

    int Parent(int i) {
        if (parent[i] != i)
            parent[i] = Parent(parent[i]);
        return parent[i];
    }

    void Union(int i, int j) {
        int pi = Parent(i), pj = Parent(j);
        if (pi == pj) return;
        n--;
        if (size[pi] < size[pj]) {
            int tmp = pi;
            pi = pj;
            pj = tmp;
        }
        parent[pj] = pi;
        size[pi] += size[pj];
    }

    int SizeOf(int i) {
        return size[Parent(i)];
    }

    int Count() {
        return n;
    }
};

int main(void) {
    int i = 1, n, m;
    cin >> n >> m;
    while (n != 0 && m != 0) {
        UnionFind uf(n);
        while (m--) {
            int a, b;
            cin >> a >> b;
            uf.Union(a - 1, b - 1);
        }
        cout << "Case " << i++ << ": " << uf.Count() << "\n";
        cin >> n >> m;
    }
}