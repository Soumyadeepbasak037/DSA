#include <iostream>
using namespace std;

struct node
{
    int data;
    node *next;
};

node *head = NULL;

void insert(int data)
{
    node *new_node = new node;
    new_node->data = data;

    if (head == NULL)
    {
        head = new node;
        head->data = data;
        head->next = head;
    }
    else
    {
        node *temp = head;
        while (temp->next != head)
        {
            temp = temp->next;
        }
        temp->next = new_node;
        new_node->next = head;
    }
}

void delete_end()
{
    node *temp = head;
    while (temp->next->next != head)
    {
        // cout << temp->data << " ";
        temp = temp->next;
    }
    temp->next = head;
}

void print()
{
    if (head == NULL)
    {
        cout << "Empty";
    }
    else
    {
        node *temp = head;
        while (temp->next != head)
        {
            cout << temp->data << " ";
            temp = temp->next;
        }
        cout << temp->data << endl; // important or else last node doesnt get printed
    }
}
int main()
{
    insert(10);
    insert(20);
    insert(340);
    print();
    delete_end();
    print();
}