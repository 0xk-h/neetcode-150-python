#include "linkedlist.hpp"
#include <stack>

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        stack<int> stk;
        ListNode* curr = head;
        while (curr != nullptr) {
            stk.push(curr->val);
            curr = curr->next;
        }

        curr = head;
        while (curr != nullptr) {
            curr->val = stk.top(); stk.pop();
            curr = curr->next;
        }

        return head;
    }
};


class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* curr = head;
        ListNode* prev = nullptr;
        ListNode* temp;
        while (curr != nullptr) {
            temp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = temp;
        }

        return prev;
    }
};