#include <iostream>
using namespace std;

struct node
{
    int data;
    node *next;
};

node *head = NULL;

void insert(int x)
{
    node *temp = new node;
    temp->next = NULL;
    temp->data = x;

    if (head == NULL)
    {
        head = temp;
        return;
    }
    else
    {
        node *tmp = head;
        while (tmp->next != NULL)
        {
            tmp = tmp->next;
        }
        tmp->next = temp;
    }
}

void delete_end()
{
    node *temp = new node;
    temp = head;
    while (temp->next->next != NULL)
    {
        temp = temp->next;
    }
    temp->next = NULL;
}
void print()
{
    node *temp = head;
    while (temp != NULL)
    {
        cout << temp->data << " ";
        temp = temp->next;
    }
    cout << endl;
}

int main()
{
    insert(10);
    insert(20);
    insert(30);

    print();
    delete_end();
    print();
    return 0;
}