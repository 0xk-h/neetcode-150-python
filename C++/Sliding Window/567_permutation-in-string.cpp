#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int m = s1.size();
        int n = s2.size();

        if (m > n) return false;

        int freq[26] = {0};
        for (char c: s1) freq[c - 'a']++;

        int l = 0;
        int matches = m;
        for (int r = 0; r < n; r++) {
            while (l < r && freq[s2[r] - 'a'] == 0) {
                freq[s2[l++] - 'a']++;
                matches++;
            }

            if (freq[s2[r] - 'a'] == 0) {
                l++;
            } else {
                freq[s2[r] - 'a']--;
                matches--;
            }
            
            if (matches == 0) return true;
        }

        return false;
    }
};


class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int m = s1.size();
        int n = s2.size();

        if (m > n) return false;

        unordered_map<char, int> freq;
        for (char c: s1) freq[c]++;

        int l = 0;
        int matches = m;
        for (int r = 0; r < n; r++) {
            if (!freq.contains(s2[r])) {
                while (l < r) freq[s2[l++]]++;
                matches = m;
                l++;
                continue;

            } else if (freq[s2[r]] == 0) {
                while (freq[s2[r]] == 0) {
                    freq[s2[l++]]++;
                    matches++;
                }
            }

            freq[s2[r]]--;
            matches--;
            if (matches == 0) return true;
        }

        return false;
    }
};