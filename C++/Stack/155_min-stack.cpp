#include <stack>

using namespace std;

class MinStack {
private:
    stack<int> stk;
    stack<int> minValue;

public:
    MinStack() {}
    
    void push(int value) {
        stk.push(value);
        if (minValue.empty() || value <= minValue.top()) minValue.push(value);
    }
    
    void pop() {
        if (minValue.top() == stk.top()) minValue.pop();
        stk.pop();
    }
    
    int top() {
        return stk.top();
    }
    
    int getMin() {
        return minValue.top();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(value);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */



 class MinStack {
private:
    stack<long long> stk;
    long long minValue;

public:
    MinStack() {}
    
    void push(int value) {
        if (stk.empty()) {
            stk.push(0);
            minValue = value;
        } else {
            long long temp = value - minValue;
            stk.push(temp);
            if(temp < 0) minValue = value;
        }
    }
    
    void pop() {
        long long x = stk.top(); stk.pop();
        if (x < 0) minValue -= x;
    }
    
    int top() {
        if (stk.top() < 0) return minValue;
        return stk.top() + minValue;
    }
    
    int getMin() {
        return minValue;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(value);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */