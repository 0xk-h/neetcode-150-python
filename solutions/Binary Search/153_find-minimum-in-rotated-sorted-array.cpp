#include <vector>
#include <climits>

using namespace std;

class Solution {
public:
    int findMin(vector<int>& nums) {
        int l = 0, r = nums.size() - 1;

        while (l < r) {
            int mid = l + (r - l) / 2;

            if (nums[mid] > nums[r]) {
                l = mid + 1;
            } else {
                r = mid;
            }
        }

        return nums[l];
    }
};


class Solution {
public:
    int findMin(vector<int>& nums) {
        int minNum = INT_MAX;
        for (int num: nums) minNum = min(minNum, num);

        return minNum;
    }
};