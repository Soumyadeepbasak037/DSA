#include <stdlib.h>
#include <stdio.h>
#include <string.h>

struct Node{
    int data;
    struct Node* left;
    struct Node* right;
};

struct Node* root = NULL;

struct Node* create_node(int data){
    struct Node* new_node = malloc(sizeof(struct Node));
    new_node->data = data;
    new_node->left = NULL;
    new_node->right = NULL;
}

struct Node* insert_node(struct Node* nd, int data) {
    if (nd == NULL) {
        return create_node(data);
    } else {
        if (data < nd->data) {
            nd->left = insert_node(nd->left, data);
        } else {
            nd->right = insert_node(nd->right, data);
        }
    }
    return nd;
}

void traversal_inorder(struct Node* nd){
    if(nd != NULL){
        traversal_inorder(nd->left);
        printf("%d ",nd->data);
        traversal_inorder(nd->right);
    }
}

void traversal_preorder(struct Node* nd){
    if(nd != NULL){
        printf("%d ",nd->data);
        traversal_inorder(nd->left);
        traversal_inorder(nd->right);
    }
}

void traversal_postorder(struct Node* nd){
    if(nd != NULL){
        traversal_inorder(nd->left);
        traversal_inorder(nd->right);
        printf("%d ",nd->data);
    }
}

int main() {
    root = insert_node(root, 50);
    root = insert_node(root, 30);
    root = insert_node(root, 70);
    root = insert_node(root, 20);
    root = insert_node(root, 40);
    root = insert_node(root, 60);
    root = insert_node(root, 80);

    printf("%d\n", root->data);

    traversal_preorder(root);
    printf("\n");

    traversal_inorder(root);
    printf("\n");

    traversal_postorder(root);
    printf("\n");
}