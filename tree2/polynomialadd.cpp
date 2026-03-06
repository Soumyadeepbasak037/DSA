#include <iostream>
using namespace std;

struct node
{
    int coeff;
    int power;
    node *next;
};

node *poly_add(node *p1, node *p2)
{
    node *result = NULL;
    node *temp = NULL;

    while (p1->next != NULL && p2->next != NULL)
    {
        node *newnode = new node();

        if (p1->power == p2->power)
        {
            newnode->coeff = p1->coeff + p2->coeff;
            newnode->power = p1->power;
            p1 = p1->next;
            p2 = p2->next;
        }
        else if (p1->power < p2->power)
        {
            newnode->coeff = p2->coeff;
            newnode->power = p2->power;
            p2 = p2->next;
        }
        else if (p1->power > p2->power)
        {
            newnode->coeff = p1->coeff;
            newnode->power = p1->power;
            p1 = p1->next;
        }
        newnode->next = NULL;

        if (result == NULL)
        {
            result = newnode;
            temp = newnode;
        }
        else
        {
            temp->next = newnode;
            temp = newnode;
        }
    }
    return result;
}