#include <iostream>

using namespace std;

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


int main()
{
  int n, m, a, b, i;
  UnionFind network;
  cin >> n >> m;
  network.initialise(n);
  while (m--) {
    cin >> a >> b;
    network._union(a, b);
  }

  bool possible = true;
  for (i = 2; i < n + 1; i++) {
    if (network.find(i) != 1) {
      cout << i << "\n";
      possible = false;
    }
  }

  if (possible) cout << "Connected";
  return 0;
}
