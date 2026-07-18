#include <stack>
#include <vector>

using namespace std;

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        size_t n = heights.size();
        stack<pair<int, int>> stk;
        int ind, i, val, res = 0;
        
        for (int i = 0; i < n; ++i) {
            ind = i;
            while (!stk.empty() && stk.top().second > heights[i]) {
                ind = stk.top().first;
                val = stk.top().second;
                stk.pop();
                res = max(res, val * (i - ind));
            }

            stk.push({ind, heights[i]});
        }

        while (!stk.empty()) {
            i = stk.top().first;
            val = stk.top().second;
            stk.pop();
            res = max(res, val * ((int)n - i));
        }

        return res;
    }
};