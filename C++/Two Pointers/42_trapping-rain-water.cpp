#include <vector>

using namespace std;

class Solution {
public:
    int trap(vector<int>& height) {
        size_t n = height.size();
        int res = 0;

        vector<int> prefix(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            prefix[i + 1] = max(prefix[i], height[i]);
        }

        vector<int> suffix(n + 1, 0);
        for (int i = n - 1; i >= 0; --i) {
            suffix[i] = max(suffix[i + 1], height[i]);
        }

        for (int i = 0; i < n; ++i) {
            res += max(0, min(prefix[i], suffix[i + 1]) - height[i]);
        }
        
        return res;
    }
};


class Solution {
public:
    int trap(vector<int>& height) {
        size_t n = height.size();
        int res = 0;
        int l = 0, r = n - 1;
        int lmax, rmax;

        while (l < r) {
            lmax = max(lmax, height[l]);
            rmax = max(rmax, height[r]);

            if (height[l] < height[r]) {
                res += lmax - height[l];
                l++;

            } else {
                res += rmax - height[r];
                r--;
            }
        }

        return res;
    }
};