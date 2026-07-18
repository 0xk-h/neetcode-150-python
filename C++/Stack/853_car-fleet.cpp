#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        size_t n = position.size();
        vector<pair<int, float>> inputs;
        int dist;
        
        for (int i = 0; i < n; ++i) {
            dist = target - position[i];
            inputs.push_back({dist, (float)dist / speed[i]});
        }
        sort(inputs.begin(), inputs.end());

        int res = 1;
        float curr = inputs[0].second;
        for (auto const& [dist, time]: inputs) {
            if (time > curr) {
                res++;
                curr = time;
            }
        }
        return res;
    }
};