#include <math.h>

#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
  vector<int> bins;
  int n = 1000;
  int l = 12;
  while (n--) {
    uint bin;
    bins.push_back(bin);
  }
  vector<uint> criteria;
  for (int j = 0; j < 12; j++) {
    int ones = 0;
    int zeros = 0;
    int w;
    for (int i = 0; i < n; i++) {
      criteria.push_back((uint)bins[i]);
      uint the_bit = (bins[i] & (uint)pow(2, j)) >> j;
      the_bit ? ones++ : zeros++;
    }
    zeros > ones ? w = 0 : w = 1;
    for (int i = 0; i < n; i++) {
      if (w != (bins[i] & (uint)pow(2, j)) >> j) {
        bins.erase(bins.begin() + i);
      }
    }
    if(criteria.size() == 1){
        break;
    }
  }