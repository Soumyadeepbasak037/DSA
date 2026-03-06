#include <iostream>
using namespace std;

struct node
{
    node *left;
    node *right;
    int data;
};

node *create_node(int data)
{
    node *new_node = new node;
    new_node->left = NULL;
    new_node->right = NULL;
    new_node->data = data;

    return new_node;
}

node *insert_node(node *root, int data)
{
    if (root == NULL)
    {
        return create_node(data);
    }

    if (data > root->data)
    {
        root->right = insert_node(root->right, data);
    }
    else
    {
        root->left = insert_node(root->left, data);
    }
    return root;
}

void inorder(node *root)
{
    if (root == NULL)
    {
        return;
    }
    inorder(root->left);
    cout << root->data << " ";
    inorder(root->right);
}

int count(node *root)
{
    if (root == NULL)
    {
        return 0;
    }
    return 1 + count(root->right) + count(root->left);
}

int search(node *root, int target)
{
    if (root == NULL)
    {
        return -1;
    }
    if (root->data == target)
    {
        return 1;
    }
    if (target > root->data)
    {
        return search(root->right, target);
    }
    else
    {
        return search(root->left, target);
    }
}
int main()
{
    node *root = NULL;
    root = insert_node(root, 56);
    root = insert_node(root, 57);
    root = insert_node(root, 55);

    inorder(root);
    cout << endl;

    cout << "Total nodes: " << count(root) << endl;
}