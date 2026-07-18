#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l = 0, r = numbers.size() - 1;

        while (l < r) {
            int sum = numbers[l] + numbers[r];

            if (sum == target) return {++l, ++r};
            else if (sum < target) l++;
            else r--;
        }

        return {0,0};
    }
};


class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        size_t n = numbers.size();
        unordered_map<int, int> map;
        int num;

        for (int i = 0; i < n; ++i) {
            num = numbers[i];
            if (map.contains(num)) return {map[num], ++i};
            map[target - num] = i + 1;
        }

        return {0,0};
    }
};