#include <cstdlib>
#include <fstream>
#include <iostream>
#include <limits>
#include <queue>
#include <sstream>
#include <stdio.h>
#include <string>
#include <vector>
const int dx[4]{-1, 0, 1, 0};
const int dy[4]{0, 1, 0, -1};
using namespace std;
using ll = long long;

void dijkstra(int i, int j, vector<vector<int>> &v, vector<vector<int>> &d) {
  priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>,
                 greater<pair<int, pair<int, int>>>>
      q;
  q.push({0, {i, j}});
  while (!q.empty()) {
    pair<int, pair<int, int>> x = q.top();
    q.pop();
    int i = x.second.first;
    int j = x.second.second;
    int dist = x.first;
    if (dist > d[i][j])
      continue;
    for (int k = 0; k < 4; k++) {
      int ni = i + dx[k];
      int nj = j + dy[k];
      if (ni < 0 || ni >= v.size() || nj >= v[0].size() || nj < 0)
        continue;
      int nd = dist + v[ni][nj];
      if (nd < d[ni][nj]) {
        d[ni][nj] = nd;
        q.push({nd, {ni, nj}});
      }
    }
  }
}

int main(int argc, char *argv[]) {
  ifstream infile(argv[1]);
  vector<vector<int>> cave;
  string line;
  while (getline(infile, line)) {
    vector<int> l;
    for (int i = 0; i < line.size(); i++) {
      l.push_back(line[i] - '0');
    }
    cave.push_back(l);
  }
  vector<vector<int>> d(
      cave.size(), vector<int>(cave[0].size(), numeric_limits<int>::max()));
  d[0][0] = 0;
  dijkstra(0, 0, cave, d);
  cout << d[d.size() - 1][d[0].size() - 1] << endl;
  return 0;
}
