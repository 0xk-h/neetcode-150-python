#include <vector>
#include <climits>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minValue = INT_MAX;
        int res = 0;

        for (int price: prices) {
            if (price < minValue) minValue = price;
            else res = max(res, price - minValue);
        }

        return res;
    }
};