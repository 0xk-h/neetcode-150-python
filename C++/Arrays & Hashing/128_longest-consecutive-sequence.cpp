#include <vector>
#include <unordered_set>
#include <algorithm>

using namespace std;

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) return 0;
        sort(nums.begin(), nums.end());

        int res = 1;
        int curr = 1;
        int prev = nums[0];
        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i - 1] == nums[i]) continue;
            if (nums[i - 1] + 1 != nums[i]) {
                curr = 0;
            }
            curr++;
            res = max(res, curr);
            prev = nums[i];
        }

        return res;
    }
};


class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> avail;
        for (int num: nums) {
            avail.insert(num);
        }

        int res = 0;
        for (int num: nums) {
            if (!avail.contains(num - 1)) {
                int l = 1;
                while (avail.contains(num + l)) l++;
                res = max(res, l);
            }
        }

        return res;
    }
};