#include <iostream>
#include <unordered_map>
#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        for (int num: nums) {
            freq[num]++;
        }

        vector<pair<int, int>> temp;
        for (const auto& [key, val]: freq) {
            temp.push_back(pair(val, key));
        }
        sort(temp.begin(), temp.end(), greater());

        vector<int> res;
        for (int i = 0; i < k; ++i) {
            res.push_back(temp[i].second);
        }

        return res;
    }
};


class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        for (int num: nums) {
            freq[num]++;
        }

        priority_queue<pair<int, int>> pq;
        for (const auto& [key, val]: freq) {
            pq.push({val, key});
        }

        vector<int> res;
        for (int i = 0; i < k; ++i) {
            res.push_back(pq.top().second);
            pq.pop();
        }

        return res;
    }
};


class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        int n = nums.size();

        unordered_map<int, int> freq;
        for (int num: nums) {
            freq[num]++;
        }

        vector<vector<int>> temp(n + 1, vector<int>());
        for (const auto& [key, val]: freq) {
            temp[val].push_back(key);
        }

        vector<int> res;
        for (int i = n; i >= 0; --i) {
            for (int x: temp[i]) {
                res.push_back(x);

                if (res.size() == k) return res;
            }
        }

        return res;
    }
};