#include <unordered_map>
#include <string>

using namespace std;

class Solution {
public:
    int characterReplacement(string s, int k) {
        size_t n = s.size();
        unordered_map<char, int> freq;

        int res = 0;
        int l = 0;
        for (int r = 0; r < n; r++) {
            freq[s[r]]++;

            while ((r - l + 1) - getMax(freq) > k) freq[s[l++]]--;

            res = max(res, r - l + 1);
        }

        return res;
    }

    int getMax(const unordered_map<char, int>& freq) {
        int res = 0;
        for (auto [ch, f]: freq) res = max(res, f);

        return res;
    }
};


class Solution {
public:
    int characterReplacement(string s, int k) {
        size_t n = s.size();
        int maxf = 0;
        unordered_map<char, int> freq;

        int res = 0;
        int l = 0;
        for (int r = 0; r < n; r++) {
            freq[s[r]]++;
            maxf = max(maxf, freq[s[r]]);

            if ((r - l + 1) - maxf > k) freq[s[l++]]--;

            res = max(res, r - l + 1);
        }

        return res;
    }
};