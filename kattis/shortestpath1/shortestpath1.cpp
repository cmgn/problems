#include <iostream>
#include <queue>
#include <vector>
#include <cstring>

#define MAX_SIZE 10001
#define INF 0x3f3f3f3f

using namespace std;

typedef pair<int, int> pii;

// global variable alert
vector<pii> graph[MAX_SIZE];
int distances[MAX_SIZE];

void dijkstra(int src)
{
  int u, v, c, w;
  priority_queue<pii, vector<pii>, greater<pii>> _queue;
  memset(distances, INF, MAX_SIZE);
  _queue.push(pii(0, src));
  distances[src] = 0;

  while (!_queue.empty()) {
    u = _queue.top().second; // node no
    c = _queue.top().first;  // accum. cost
    _queue.pop();

    if (distances[u] < c) continue; // already have a better solution

    for (int i = 0; i < graph[u].size(); i++) {
      v = graph[u][i].first; // node no
      w = graph[u][i].second;
      
      if (distances[v] > distances[u] + w) {
        distances[v] = distances[u] + w;
        _queue.push(pii(distances[v], v));
      }
    }
  }
}

int main()
{
  // n: number of nodes.
  // m: number of edges.
  // q: number of queries.
  // s: index of the start.
  int n, m, q, s;
  while (scanf("%d %d %d %d", &n, &m, &q, &s) == 4) {
    if (!n && !m && !q && !s) return 0;
    // empty out previously used graph 
    for (int i = 0; i < MAX_SIZE; i++) graph[i].clear();

    for (int i = 0; i < m; i++) {
      int u, v, w;
      scanf("%d %d %d", &u, &v, &w);
      graph[u].push_back(pii(v, w));
    }

    dijkstra(s);

    for (int i = 0; i < q; i++) {
      int dst;
      cin >> dst;
      if (distances[dst] == INF)
        std::cout << "Impossible\n";
      else
        std::cout << distances[dst] << "\n";
    }
    std::cout << "\n";
  }

  return 0;
}
