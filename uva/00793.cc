#include <bits/stdc++.h>

using namespace std;

class UnionFind {
private:
    vector<int> parent, size;

public:
    UnionFind(int n) {
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

    bool Connected(int i, int j) {
        return Parent(i) == Parent(j);
    }
};

int main(void) {
    int n, m, i, j;
    char c;
    string line;
    stringstream ss;

    getline(cin, line);
    ss.str(line);
    ss >> n;
    getline(cin, line);

    while (n--) {
        int yes = 0, no = 0;

        getline(cin, line);
        ss.clear();
        ss.str(line);
        ss >> m;
        UnionFind uf(m);

        getline(cin, line);
        ss.clear();
        ss.str(line);
        while (ss >> c >> i >> j) {
            i--, j--;
            if (c == 'c')
                uf.Union(i, j);
            else if (c == 'q') {
                if (uf.Connected(i, j))
                    yes++;
                else
                    no++;
            }
            if (!getline(cin, line)) break;
            ss.clear();
            ss.str(line);
        }
        cout << yes << "," << no << "\n";
        if (n) cout << "\n";
    }
}