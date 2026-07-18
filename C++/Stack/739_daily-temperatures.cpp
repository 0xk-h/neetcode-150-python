#include <vector>
#include <stack>

using namespace std;

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        size_t n = temperatures.size();
        stack<int> stk;
        vector<int> res(n, 0);
        int i;

        for (int j = 0; j < n; ++j) {
            while (!stk.empty() && temperatures[stk.top()] < temperatures[j]) {
                i = stk.top(); stk.pop();
                res[i] = j - i;
            }
            stk.push(j);
        }
        return res;
    }
};


// TLE
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        size_t n = temperatures.size();
        stack<int> stk;
        vector<int> res(n, 0);

        for (int i = 0; i < n; ++i) {
            int curr = temperatures[i];
            for (int j = i + 1; j < n; ++j) {
                if (temperatures[j] > curr) {
                    res[i] = j - i;
                    break;
                }
            }
        }
        return res;
    }
};