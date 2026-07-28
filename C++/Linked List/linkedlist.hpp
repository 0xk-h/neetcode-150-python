#pragma once
#include <iostream>

using namespace std;

class ListNode {
    public:
        int val;
        ListNode *next;
        ListNode() : val(0), next(nullptr) {}
        ListNode(int x) : val(x), next(nullptr) {}
        ListNode(int x, ListNode *next) : val(x), next(next) {}

        inline size_t size() const {
            size_t count = 0;
            const ListNode* curr = this;
            while (curr) {
                count++;
                curr = curr->next;
            }
            return count;
        }

        inline int operator[](const ListNode* node, size_t index) const {
            size_t count = 0;
            while (node) {
                if (count == index) return node->val;
                count++;
                node = node->next;
            }
            throw "Error: Index out of range!! \n" + to_string(index) + " is out of range, since the size is " + to_string(size()) + "\n";
        }
};

inline ostream& operator<<(ostream& os, const ListNode* node) {
    while (node) {
        os << node->val;
        if (node->next) os << " -> ";
        node = node->next;
    }

    return os;
}