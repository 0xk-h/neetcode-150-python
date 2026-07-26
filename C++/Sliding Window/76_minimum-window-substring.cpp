#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
    string minWindow(string s, string t) {
        // 'z' - 'A' = 57;
        int m = t.size();
        int n = s.size();

        if (m > n) return "";

        int matches = 0;
        int tmap[58] = {0};
        for (char c: t) {
            if (tmap[c - 'A'] == 0) matches++;
            tmap[c - 'A']++;
        }

        int smap[58] = {0};

        int l = 0;
        int start = -1, len = n + 1;
        for (int r = 0; r < n; r++) {
            smap[s[r] - 'A']++;
            if (tmap[s[r] - 'A'] > 0 && smap[s[r] - 'A'] == tmap[s[r] - 'A']) matches--;

            while (l < r && smap[s[l] - 'A'] > tmap[s[l] - 'A']) {
                smap[s[l] - 'A']--;
                l++;
            }

            if (matches == 0) {
                if (len > r - l + 1) {
                    len = r - l + 1;
                    start = l;
                }

                smap[s[l] - 'A']--;
                if (smap[s[l] - 'A'] < tmap[s[l] - 'A']) matches++;
                l++;
            }
        }

        if (start == -1) return "";
        return s.substr(start, len);
    }
};


class Solution {
public:
    string minWindow(string s, string t) {
        int m = t.size();
        int n = s.size();

        if (m > n) return "";

        unordered_map<char, int> map;
        for (char c: t) map[c]++;
        int matches = map.size();

        int l = 0;
        int len = n + 1;
        int start = -1;
        for (int r = 0; r < n; r++) {
            if (map.contains(s[r])) {
                map[s[r]]--;
                if (map[s[r]] == 0) matches--;
            }

            while (l < r && (!map.contains(s[l]) || map[s[l]] < 0)) {
                if (map.contains(s[l]) && map[s[l]] < 0) map[s[l]]++;
                l++;
            }

            if (matches == 0) {
                if (len > r - l + 1) {
                    len = r - l + 1;
                    start = l;
                }
                if (map[s[l]] >= 0) matches++;
                map[s[l++]]++;
            }
        }

        if (start == -1) return "";
        return s.substr(start, len);
    }
};


class Solution {
public:
    string minWindow(string s, string t) {
        int m = t.size();
        int n = s.size();

        if (m > n) return "";

        unordered_map<char, int> tmap;
        for (char c: t) tmap[c]++;

        unordered_map<char, int> smap;
        int matches = tmap.size();

        int l = 0;
        int start = -1, len = n + 1;
        for (int r = 0; r < n; r++) {
            smap[s[r]]++;
            if (tmap.contains(s[r]) && smap[s[r]] == tmap[s[r]]) matches--;

            while (l < r && smap[s[l]] > tmap[s[l]]) {
                smap[s[l]]--;
                l++;
            }

            if (matches == 0) {
                if (len > r - l + 1) {
                    len = r - l + 1;
                    start = l;
                }

                smap[s[l]]--;
                if (smap[s[l]] < tmap[s[l]]) matches++;
                l++;
            }
        }

        if (start == -1) return "";
        return s.substr(start, len);
    }
};