#include <vector>
#include <unordered_set>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        size_t n = nums.size();

        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (nums[i] + nums[j] == target) {
                    return {i, j};
                }
            }
        }
        return {};
    }
};


class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        size_t n = nums.size();
        unordered_map<int, int> map;

        for (int i = 0; i < n; ++i) {
            if (map.contains(nums[i])) {
                return {map[nums[i]], i};
            }
            map[target - nums[i]] = i;
        }
        return {};
    }
};