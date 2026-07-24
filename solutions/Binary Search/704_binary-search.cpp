#include <vector>

using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int res = -1;
        int l = 0, r = nums.size() - 1;

        while (l <= r) {
            int mid = (l + r) / 2;

            if (nums[mid] == target) {
                res = mid;
                break;
            } else if (nums[mid] < target) l = mid + 1;
            else r = mid - 1;
        }
        return res;
    }
};


class Solution {
public:
    int search(vector<int>& nums, int target) {
        size_t n = nums.size();
        int res = -1;
        int l = 0, r = n - 1;

        while (l < r) {
            int mid = (l + r) / 2;

            if (nums[mid] < target) l = mid + 1;
            else r = mid;
        }
        
        if (l >= 0 && l < n && nums[l] == target) return l;
        return -1;
    }
};