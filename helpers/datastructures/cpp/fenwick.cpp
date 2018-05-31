#include <vector>

using namespace std;

struct FenwickTree {
    vector<int> v;

    FenwickTree(vector<int> u)
    {
        v = vector<int>(u.size() + 1);
        for (int i = 0; i < u.size(); i++)
            add(i+1, u[i]);
    }

    void add(int i, int n)
    {
        while (i < v.size()) {
            v[i] += n;
            i += (i & -i);
        }
    }

    int sum(int i)
    {
        int result = 0;
        while (i) {
            result += v[i];
            i -= (i & -i);
        }
        return result;
    }
};
