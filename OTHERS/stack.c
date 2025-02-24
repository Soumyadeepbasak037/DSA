#include <stdlib.h>
#include <stdio.h>
#include <string.h>

struct Node
{
    int data;
    struct Node *prev;
    struct Node *next;
};

struct Node *head = NULL;
struct Node *tail = NULL;

struct Node *create_node(int data)
{
    struct Node *nd;
    nd = (struct Node *)malloc(sizeof(struct Node));
    nd->data = data;
    nd->prev = NULL;
    nd->next = NULL;
    return nd;
}

void push(int data)
{
    struct Node *new_node = create_node(data);
    if (head == NULL)
    {
        head = new_node;
        tail = new_node;
    }
    else
    {
        new_node->prev = tail;
        tail->next = new_node;
        tail = new_node;
    }
}

int pop()
{
    if (tail == NULL)
    {
        printf("Stack underflow\n");
    }
    struct Node *temp = tail;
    int poppedData = temp->data;
    if (tail->prev)
    {
        tail = tail->prev;
        tail->next = NULL;
    }
    else
    {
        head = NULL;
        tail = NULL;
    }
    free(temp);
    printf("Popped: %d\n", poppedData);
    return poppedData;
}

void displayStack()
{
    struct Node *temp = head;
    while (temp != NULL)
    {
        printf("%d -> ", temp->data);
        temp = temp->next;
    }
    printf("NULL\n");
}

int main()
{
    for (int i = 0; i < 60; i++)
    {
        push(i);
    }
    displayStack();
}