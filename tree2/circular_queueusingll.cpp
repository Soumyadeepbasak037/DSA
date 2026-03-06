#include <iostream>
using namespace std;

struct node
{
    node *next;
    int data;
};

node *front = NULL;
node *rear = NULL;

void enqueue(int data)
{
    node *new_node = new node;
    new_node->data = data;
    if (front == NULL)
    {
        front = new_node;
        rear = new_node;
        rear->next = front;
        front->next = rear;
    }

    else
    {
        rear->next = new_node;
        rear = new_node;
        rear->next = front;
    }
}