#include <vector>

using namespace std;

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        size_t m = matrix.size(), n = matrix[0].size();
        bool res = false;

        int l = 0, r = (m * n) - 1;
        int mid, val;
        while (l <= r) {
            mid = (l + r) / 2;
            val = matrix[mid / n][mid % n];
            if (val == target) {
                res = true;
                break;
            } else if (val < target) l = mid + 1;
            else r = mid - 1;
        }

        return res;
    }
};


class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        size_t m = matrix.size(),n = matrix[0].size();
        bool res = false;

        int l = 0, r = m - 1;
        int row = 0;
        while (l <= r) {
            int mid = (l + r) / 2;

            if (matrix[mid][0] <= target && target <= matrix[mid][n - 1]) {
                res = true;
                row = mid;
                break;
            } else if (matrix[mid][0] > target) r = mid - 1;
            else l = mid + 1;
        }

        if (!res) return false;
        res = false;
        l = 0, r = n - 1;
        while (l <= r) {
            int mid = (l + r) / 2;

            if (matrix[row][mid] == target) {
                res = true;
                break;
            } else if (matrix[row][mid] < target) l = mid + 1;
            else r = mid - 1;
        }

        return res;
    }
};