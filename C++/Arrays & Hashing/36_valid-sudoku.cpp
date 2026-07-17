#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int n = 9;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (board[i][j] != '.' && !check(board, i, j)) {
                    return false;
                }
            }
        }
        return true;
    }
    bool check(vector<vector<char>>& board, int x, int y) {
        int n = 9;
        char val = board[x][y];
        int x1 = (x / 3) * 3;
        int y1 = (y / 3) * 3;

        for (int i = x1; i < x1+3; ++i) {
            if (i == x) continue;
            for (int j = y1; j < y1+3; ++j) {
                if (j != y && board[i][j] == val) return false;
            }
        }

        int j = y;
        for (int i = 0; i < n; ++i) {
            if (i != x && board[i][j] == val) return false;
        }

        int i = x;
        for (int j = 0; j < n; ++j) {
            if (j != y && board[i][j] == val) return false;
        }

        return true;
    }
};


class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int n = 9;
        vector<unordered_set<char>> row(9);
        vector<unordered_set<char>> col(9);
        vector<unordered_set<char>> box(9);

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (board[i][j] != '.') {
                    char val = board[i][j];
                    int b = ((i / 3) * 3) + (j / 3);

                    if (row[i].contains(val) || col[j].contains(val) || box[b].contains(val)) {
                        return false;
                    }
                    row[i].insert(val);
                    col[j].insert(val);
                    box[b].insert(val);
                }
            }
        }
        return true;
    }
};


class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int n = 9;
        vector<int> row(9);
        vector<int> col(9);
        vector<int> box(9);

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (board[i][j] != '.') {
                    int b = ((i / 3) * 3) + (j / 3);
                    int val = board[i][j] - '0';

                    if (row[i] & 1 << val || col[j] & 1 << val || box[b] & 1 << val) {
                        return false;
                    }
                    row[i] |= 1 << val;
                    col[j] |= 1 << val;
                    box[b] |= 1 << val;
                }
            }
        }
        return true;
    }
};