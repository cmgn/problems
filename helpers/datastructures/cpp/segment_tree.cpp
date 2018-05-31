#include <vector>

using namespace std;

struct segment_tree {
    segment_tree *left, *right;
    int from, to, value;
    segment_tree(int from, int to) 
        : from(from), to(to), left(NULL), right(NULL), value(0) {}
};

segment_tree *make(const vector<int> &v, int l, int r)
{
    if (l > r) return NULL;
    segment_tree *res = new segment_tree(l, r);
    if (l == r)
        res->value = v[l];
    else {
        int m = (l + r) / 2;
        res->left = make(v, l, m);
        res->right = make(v, m + 1, r);
        if (res->left != NULL) res->value += res->left->value;
        if (res->right != NULL) res->value += res->right->value;
    }
    return res;
}

int make_query(segment_tree *t, int l, int r)
{
    if (t == NULL) return 0;
    else if (l <= t->from && t->to <= r) return t->value;
    else if (t->to < l || r < t->from) return 0;
    
    return make_query(t->left, l, r) + make_query(t->right, l, r);
}

int make_update(segment_tree *t, int i, int v)
{
    if (t == NULL) return 0;
    else if (t->to < i || i < t->from) return t->value;
    
    if (t->from == t->to && t->from == i)
        t->value = v;
    else
        t->value = make_update(t->left, i, v) + make_update(t->right, i, v);
    return t->value;
}
