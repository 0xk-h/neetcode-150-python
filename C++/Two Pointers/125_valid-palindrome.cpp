#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
        string pali;

        for (char c: s) {
            if (isalnum(c)) pali += tolower(c);
        }

        string paliRev = pali;
        reverse(paliRev.begin(), paliRev.end());

        return pali == paliRev;
    }
};


class Solution {
public:
    bool isPalindrome(string s) {
        int l = 0, r = s.size() - 1;

        while (l < r) {
            while (l < r && !isalnum(s[l])) l++;
            while (l < r && !isalnum(s[r])) r--;

            if (tolower(s[l]) != tolower(s[r])) return false;
            l++;
            r--;
        }

        return true;
    }
};