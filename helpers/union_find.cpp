// not the actual union find algorithm as this was for a specific question,
// but it is easy to hack into what ever needs be

struct UnionFind {
  int parent[200001];
  
  void initialise(int n) 
  {
    for (int i = 1; i < n + 1; i++)
      parent[i] = i;
  }

  void _union(int a, int b)
  {
    a = find(a);
    b = find(b);
    if (a == b) return;
    
    if (b < a) {
      int temp = a;
      a = b;
      b = temp;
    }

    parent[b] = a;
  }

  int find(int a) 
  {
    while (a != parent[a]) {
      parent[a] = parent[parent[a]];
      a = parent[a];
    }
    return a;
  }
};