#include <stdio.h>
#include <iostream>
using namespace std;

class Node
{
public:
    Node *left;
    Node *right;
    int data;
    Node(Node *right, Node *left, int data)
    {
        this->data = data;
        this->right = right;
        this->left = left;
    }
};

class Tree
{
};
int main()
{
}