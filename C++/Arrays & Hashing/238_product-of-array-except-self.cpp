#include <vector>

using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        size_t n = nums.size();
        vector<int> res(n, 1);

        int acc = 1;
        for (int i = 0; i < n; ++i) {
            res[i] *= acc;
            acc *= nums[i];
        }

        acc = 1;
        for (int i = n - 1; i >= 0; --i) {
            res[i] *= acc;
            acc *= nums[i];
        }

        return res;
    }
};