#include <iostream>
#include <stack>
#include <vector>

using namespace std;

class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> stk;
        int a, b;

        for (string ch: tokens) {
            if (ch == "+") {
                b = stk.top(); stk.pop();
                a = stk.top(); stk.pop();
                stk.push(a + b);
            } else if (ch == "-") {
                b = stk.top(); stk.pop();
                a = stk.top(); stk.pop();
                stk.push(a - b);
            } else if (ch == "*") {
                b = stk.top(); stk.pop();
                a = stk.top(); stk.pop();
                stk.push(a * b);
            } else if (ch == "/") {
                b = stk.top(); stk.pop();
                a = stk.top(); stk.pop();
                stk.push(a / b);
            } else {
                stk.push(stoi(ch));
            }
        }

        return stk.top();
    }
};