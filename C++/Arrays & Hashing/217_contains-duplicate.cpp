#include <vector>
#include <unordered_set>
#include <unordered_map>

using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        return nums.size() != unordered_set(nums.begin(), nums.end()).size();
    }
};


class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> seen;

        for (int num: nums) {
            auto res = seen.insert(num);
            
            if (!res.second) {
                return true;
            }
        }

        return false;
    }
};


class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> freq;

        for (int num: nums) {
            freq[num]++;
        }
        for (auto const& [key, val]: freq) {
            if (val > 1) {
                return true;
            }
        }
        return false;
    }
};