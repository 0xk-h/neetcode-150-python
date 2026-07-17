#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    string encode(vector<string>& strs) {
        string res;
        for (string& s : strs) {
            res += to_string(s.size()) + "-" + s;
        }
        return res;
    }

    vector<string> decode(string s) {
        vector<string> res;
        int i = 0;

        while (i < s.size()) {
            string d;

            while (s[i] != '-') {
                d += s[i];
                i++;
            }

            int len = stoi(d);
            string curr;

            for (int k = 0; k < len; k++) {
                i++;
                curr += s[i];
            }

            i++;
            res.push_back(curr);
        }

        return res;
    }
};
