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
    int cases;
    cin >> cases;
    while (cases--) {
        UnionFind uf(100005);
        unordered_map<string, int> id;
        int friendships;
        cin >> friendships;
        while (friendships--) {
            string a, b;
            cin >> a >> b;
            if (id.count(a) == 0) id[a] = id.size();
            if (id.count(b) == 0) id[b] = id.size();
            int ida = id[a], idb = id[b];
            uf.Union(id[a], id[b]);
            cout << uf.SizeOf(id[a]) << "\n";
        }
    }
}