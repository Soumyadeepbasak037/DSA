
#include <vector>
using namespace std;
#include <iostream>
#include <queue>

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution
{
public:
    vector<vector<int>> bfs(TreeNode *root)
    {

        queue<TreeNode *> q;
        q.push(root);
        while (!q.empty())
        {
            TreeNode *p = q.front();
            cout << p->val << endl;

            q.pop();
            if (p->left)
            {
                q.push(p->left);
            }
            if (p->right)
            {
                q.push(p->right);
            }
        }
    }
    vector<vector<int>> levelOrder(TreeNode *root)
    {
        vector<vector<int>> ans;
        queue<TreeNode *> q;
        q.push(root);
        size_t sz = q.size();

        vector<int> processed;
        while (!q.empty())
        {
            for (int i = 0; i < sz; i++)
            {
                TreeNode *p = q.front();
                q.pop();
                processed.push_back(p->val);

                if (p->left)
                {
                    q.push(p->left);
                }
                if (p->right)
                {
                    q.push(p->right);
                }
            }
            ans.push_back(processed);
        };
        return ans;
    }
};

int main()
{

    TreeNode *node4 = new TreeNode(4);
    TreeNode *node5 = new TreeNode(5);

    TreeNode *node2 = new TreeNode(2, node4, node5);
    TreeNode *node3 = new TreeNode(3);

    TreeNode *root = new TreeNode(1, node2, node3);

    cout << "Root value: " << root->val << endl;

    Solution s;
    s.levelOrder(root);
}