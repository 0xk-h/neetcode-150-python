#include <bits/stdc++.h>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

TreeNode* from_list(const std::vector<std::optional<int>>& lst) {
    if (lst.empty() || !lst[0].has_value()) {
        return nullptr;
    }

    TreeNode* root = new TreeNode(*lst[0]);
    queue<TreeNode*> q;
    q.push(root);
    size_t i = 1;

    while (!q.empty() && i < lst.size()) {
        TreeNode* node = q.front();
        q.pop();

        if (i < lst.size()) {
            if (lst[i].has_value()) {
                node->left = new TreeNode(*lst[i]);
                q.push(node->left);
            }
            ++i;
        }

        if (i < lst.size()) {
            if (lst[i].has_value()) {
                node->right = new TreeNode(*lst[i]);
                q.push(node->right);
            }
            ++i;
        }
    }

    return root;
}