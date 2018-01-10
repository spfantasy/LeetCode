/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int countNodes(TreeNode* root) {
        int l = 0, r = 0;
        TreeNode *lp = root;
        TreeNode *rp = root;
        while(lp != nullptr){
            lp = lp->left;
            ++l;
        }
        while(rp != nullptr){
            rp = rp->right;
            ++r;
        }
        if(l == r)
            return pow(2,l)-1;
        return 1 + countNodes(root->left) + countNodes(root->right);
    }
};