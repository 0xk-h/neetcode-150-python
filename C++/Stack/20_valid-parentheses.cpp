#include <unordered_map>
#include <stack>

using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> stk;
        unordered_map<char, char> map = {
            {'(', ')'},
            {'{', '}'},
            {'[', ']'}
        };

        for (char c: s) {
            if (map.contains(c)) stk.push(c);
            else if (!stk.empty() && map[stk.top()] == c) stk.pop();
            else return false;
        }

        return stk.empty();
    }
};