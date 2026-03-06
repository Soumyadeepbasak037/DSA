#include <iostream>
using namespace std;

struct node
{
    node *next = NULL;
    node *prev = NULL;
    int data;
};

node *head = NULL;

void insert_end(int data)
{
    node *new_node = new node;
    new_node->data = data;

    if (head == NULL)
    {
        head = new_node;
        // cout << head->data;
    }
    else
    {
        node *temp = head;
        while (temp->next != NULL)
        {
            temp = temp->next;
        }
        temp->next = new_node;
        new_node->prev = temp;
    }
}
// void insrt_beg()
// {
// }
void delete_end()
{
    if (head != NULL)
    {
        node *temp = head;
        while (temp->next->next != NULL)
        {
            temp = temp->next;
        }

        // cout << temp->data;
        temp->next = NULL;
    }
}
void print()
{
    node *temp = head;
    while (temp->next != NULL)
    {
        cout << temp->data << "->";
        temp = temp->next;
    }
    cout << temp->data;
}
int main()
{
    insert_end(5);
    insert_end(19);
    insert_end(19);
    insert_end(19);
    insert_end(132);
    delete_end();
    print();
}