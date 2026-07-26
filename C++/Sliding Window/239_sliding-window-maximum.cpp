#include <deque>
#include <vector>
#include <unordered_set>
#include <queue>

using namespace std;

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int n = nums.size();
        deque<int> window;
        for (int i = 0; i < k - 1; i++) {
            while (!window.empty() && window.back() < nums[i]) window.pop_back();
            window.push_back(nums[i]);
        }

        vector<int> res;
        for (int i = k - 1; i < n; i++) {
            while (!window.empty() && window.back() < nums[i]) window.pop_back();
            window.push_back(nums[i]);

            res.push_back(window.front());
            if (window.front() == nums[i - k + 1]) window.pop_front();
        }

        return res;
    }
};


class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int n = nums.size();
        unordered_set<int> deleted;
        priority_queue<pair<int, int>, vector<pair<int, int>>, less<pair<int, int>>> heap;
        for (int i = 0; i < k - 1; i++) {
            heap.push({nums[i], i});
        }

        vector<int> res;
        for (int i = k - 1; i < n; i++) {
            heap.push({nums[i], i});

            while (deleted.contains(heap.top().second)) heap.pop();

            res.push_back(heap.top().first);
            deleted.insert(i - k + 1);
        }

        return res;
    }
};