#include <bits/stdc++.h>

using namespace std;

#define BLANK 0
#define BLACK 1
#define WHITE 2
#define PARENT 3

int pos = 0;

void quadtree(vector<int> &tree, string &str, int node) {
    char c = str[pos];
    pos++;
    if (c == 'f') {
        tree[node] = BLACK;
    } else if (c == 'e') {
        tree[node] = WHITE;
    } else {
        tree[node] = PARENT;
        for (int i = 0; i < 4; i++) {
            quadtree(tree, str, 4*node + i + 1);
        }
    }
}

void merge(vector<int> &dst, vector<int> &t1, vector<int> &t2, int node) {
    int a = t1[node], b = t2[node];
    if (a == BLACK || b == BLACK) {
        dst[node] = BLACK;
    } else if (a == WHITE && b == BLANK || a == BLANK && b == WHITE
                                        || a == WHITE && b == WHITE) {
        dst[node] = WHITE;
    } else if (a == PARENT || b == PARENT) {
        dst[node] = PARENT;
        for (int i = 0; i < 4; i++) {
            merge(dst, t1, t2, 4*node + i + 1);
        }
    }
}

int black_area(vector<int> &tree, int node, int curr) {
    if (tree[node] == BLACK) {
        return curr;
    } else if (tree[node] == WHITE) {
        return 0;
    }
    int total = 0;
    for (int i = 0; i < 4; i++) {
        total += black_area(tree, 4*node + i + 1, curr / 4);
    }
    return total;
}

int main(void) {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        string s;
        vector<int> t1(2000), t2(2000), t3(2000);
        fill(t1.begin(), t1.end(), BLANK);
        fill(t2.begin(), t2.end(), BLANK);
        fill(t3.begin(), t3.end(), BLANK);
        cin >> s;
        pos = 0;
        quadtree(t1, s, 0);
        cin >> s;
        pos = 0;
        quadtree(t2, s, 0);
        merge(t3, t1, t2, 0);
        cout << "There are " << black_area(t3, 0, 1024) << " black pixels.\n";
    }
}
