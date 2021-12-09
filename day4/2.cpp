#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int getScore(vector<vector<pair<int, bool>>> &board) {
  int score = 0;
  for (int i = 0; i < board.size(); i++) {
    for (int j = 0; j < board[0].size(); j++) {
      if (board[i][j].second == false) {
        score += board[i][j].first;
      }
    }
  }
  return score;
}

void markNumber(vector<vector<pair<int, bool>>> &board, int n) {
  for (int i = 0; i < board.size(); i++) {
    for (int j = 0; j < board[0].size(); j++) {
      if (board[i][j].first == n) {
        board[i][j].second = true;
      }
    }
  }
}

// return <haswon?, thesum>
pair<bool, int> hasWon(vector<vector<pair<int, bool>>> &board) {
  // check whole row
  for (int i = 0; i < board.size(); i++) {
    for (int j = 0; j < board[0].size(); j++) {
      if (board[i][j].second == false) {
        break;
      }
      if (j == board[0].size() - 1 && board[i][j].second) {
        int score = getScore(board);
        return pair<bool, int>(true, score);
      }
    }
  }
  // check column
  for (int j = 0; j < board[0].size(); j++) {
    for (int i = 0; i < board.size(); i++) {
      if (board[i][j].second == false) {
        break;
      }
      if (i == board.size() - 1 && board[i][j].second) {
        int score = getScore(board);
        return pair<bool, int>(true, score);
      }
    }
  }
  return pair<bool, int>(false, 69);
}

int main() {
  int n = 100;
  int n_boards = 100;
  vector<int> nums;
  while (n--) {
    int num;
    cin >> num;
    nums.push_back(num);
  }
  // create all boards
  vector<vector<vector<pair<int, bool>>>> boards;
  while (n_boards--) {
    // create a single board
    vector<vector<pair<int, bool>>> board;
    for (int i = 0; i < 5; i++) {
      vector<pair<int, bool>> line;
      for (int i = 0; i < 5; i++) {
        int n;
        cin >> n;
        line.push_back(pair<int, bool>(n, false));
      }
      board.push_back(line);
    }
    boards.push_back(board);
  }

  int nn = 0;

  while (boards.size() > 1) {
    vector<vector<vector<pair<int, bool>>>>::iterator it = boards.begin();
    cout << boards.size() << endl;
    while (it != boards.end()) {
      markNumber(*it, nums[nn]);
      if (hasWon(*it).first) {
        cout << "won with: " << nums[nn] << endl;
        it = boards.erase(it);
      } else {
        ++it;
      }
    }
    nn++;
  }

  cout << boards.size() << " <-" << endl;
  for (int i = nn; i < nums.size(); i++) {
    cout << "after num: " << nums[i] << endl;
    markNumber(boards[0], nums[i]);
    auto winner = hasWon(boards[0]);
    if (winner.first) {
      cout << winner.second << " " << nums[i] << endl;
      cout << winner.second * nums[i] << endl;
      return 0;
    }
  }

  return 0;
}


// test ammend
