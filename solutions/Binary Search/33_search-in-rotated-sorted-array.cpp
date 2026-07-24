#include <vector>

using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        size_t n = nums.size();
        int l = 0, r = n - 1;

        while (l <= r) {
            int mid = l + (r - l) / 2;

            if (nums[mid] == target) return mid;

            else if (nums[l] <= nums[mid]) {
                if (target >= nums[l] && target < nums[mid]) r = mid - 1;
                else l = mid + 1;

            } else {
                if (target > nums[mid] && target <= nums[r]) l = mid + 1;
                else r = mid - 1;
            }
        }

        return -1;
    }
};


class Solution {
public:
    int search(vector<int>& nums, int target) {
        size_t n = nums.size();
        int l = 0, r = n - 1;

        while (l < r) {
            int mid = l + (r - l) / 2;

            if (nums[mid] > nums[r]) l = mid + 1;
            else r = mid;
        }

        if (target <= nums[n - 1]) {
            r = n - 1;
        } else {
            r = l;
            l = 0;
        }

        while (l <= r) {
            int mid = l + (r - l) / 2;

            if (nums[mid] == target) return mid;

            else if (nums[mid] < target) l = mid + 1;
            else r = mid - 1;
        }

        return -1;
    }
};