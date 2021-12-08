#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main() {
  string command;
  int len;
  int x = 0;
  int aim = 0;
  int depth = 0;
  int n = 1000;
  while (n--) {
    cin >> command; cin >> len;
    cout << command << " " << len << endl;
    if (command == "forward") {
      x += len;
      depth += aim*len;
    }
    if (command == "down") {
      aim += len;
    }
    if (command == "up") {
      aim -= len;
    }
  }
  cout << x*depth << endl;
}
