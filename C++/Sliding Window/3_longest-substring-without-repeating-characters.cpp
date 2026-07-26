#include <unordered_set>
#include <unordered_map>
#include <string>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        size_t n = s.size();
        unordered_set<char> seen;
        int res = 0;

        int l = 0;
        for (int r = 0; r < n; r++) {
            while (seen.contains(s[r])) {
                seen.erase(s[l]);
                l++;
            }
            
            seen.insert(s[r]);
            res = max(res, r - l + 1);
        }

        return res;
    }
};


class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        size_t n = s.size();
        unordered_map<char, int> map;
        int res = 0;

        int l = 0;
        for (int r = 0; r < n; r++) {
            if (map.contains(s[r])) {
                l = max(l, map[s[r]] + 1);
            }
            map[s[r]] = r;
            res = max(res, r - l + 1);
        }

        return res;
    }
};