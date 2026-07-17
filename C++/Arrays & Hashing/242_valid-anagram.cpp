#include <iostream>
#include <unordered_map>
#include <array>
#include <algorithm>

using namespace std;


class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;

        unordered_map<char, int> sm;
        unordered_map<char, int> tm;
        for (char c: s) {
            sm[c]++;
        }
        for (char c: t) {
            tm[c]++;
        }

        for (const auto& [key, val]: sm) {
            if (tm[key] != val) return false;
        }
        return true;
    }
};


class Solution {
public:
    bool isAnagram(string s, string t) {
        array<int, 26> sa;
        array<int, 26> ta;

        sa.fill(0);
        ta.fill(0);

        for (char c: s) {
            sa[c - 'a']++;
        }
        for (char c: t) {
            ta[c - 'a']++;
        }

        return sa == ta;
    }
};


class Solution {
public:
    bool isAnagram(string s, string t) {
        array<int, 26> arr;
        arr.fill(0);

        for (char c: s) {
            arr[c - 'a']++;
        }
        for (char c: t) {
            arr[c - 'a']--;
        }

        return all_of(arr.begin(), arr.end(), [](int x) {return x == 0;});
    }
};