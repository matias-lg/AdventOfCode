#include <cstdlib>
#include <fstream>
#include <iostream>
#include <limits>
#include <math.h>
#include <queue>
#include <sstream>
#include <stdio.h>
#include <string>
#include <vector>

const int dx[4]{-1, 0, 1, 0};
const int dy[4]{0, 1, 0, -1};
using namespace std;
using ll = long long;

void dijkstra(int i, int j, vector<vector<int>> &v, vector<vector<ll>> &d) {
  priority_queue<pair<ll, pair<int, int>>, vector<pair<int, pair<int, int>>>,
                 greater<pair<int, pair<int, int>>>>
      q;
  q.push({0, {i, j}});
  while (!q.empty()) {
    pair<ll, pair<int, int>> x = q.top();
    q.pop();
    int i = x.second.first;
    int j = x.second.second;
    ll dist = x.first;
    if (dist > d[i][j])
      continue;
    for (int k = 0; k < 4; k++) {
      int ni = i + dx[k];
      int nj = j + dy[k];
      if (ni < 0 || ni >= v.size() || nj >= v[0].size() || nj < 0)
        continue;
      ll nd = dist + v[ni][nj];
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
  vector<vector<int>> cave2(cave.size() * 5, vector<int>(0));

  for (int i = 0; i < cave2.size(); i++) {
    int cl = i % cave.size();
    int ii = 0;
    while (ii < 5) {
      for (auto &&n : cave[cl]) {
        int new_n = (n + ii + i / cave.size());
        if (new_n > 9)
          new_n = new_n % 10 + 1;
        cave2[i].push_back(new_n);
      }
      ii++;
    }
  }
  vector<vector<ll>> d(cave2.size(),
                       vector<ll>(cave2[0].size(), numeric_limits<int>::max()));
  d[0][0] = 0;
  dijkstra(0, 0, cave2, d);
  cout << d[d.size() - 1][d[0].size() - 1] << endl;
  return 0;
}
