#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main() {
  string command;
  int dir;
  int x = 0;
  int y = 0;
  int n = 1000;
  while (n--) {
    cin >> command; cin >> dir;
    cout << command << " " << dir << endl;
    if (command == "forward") {
      x += dir;
    }
    if (command == "down") {
      y += dir;
    }
    if (command == "up") {
      y -= dir;
    }
  }
  cout << x*y << endl;
}
