#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int l = 1, r = *max_element(piles.begin(), piles.end());
        int res;

        while (l <= r) {
            int k = l + (r - l) / 2;

            if (timeTaken(piles, k) <= h) {
                r = k - 1;
                res = k;
            } else {
                l = k + 1;
            }
        }

        return res;
    }

    long long timeTaken(const vector<int>& piles, int s) {
        long long ans = 0;

        for (int p: piles) {
            ans += (p / s) + (p % s > 0);
        }

        return ans;
    }
};