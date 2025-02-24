#include <stdlib.h>
#include <stdio.h>

struct Node {
    int data;
    struct Node* next;
};

struct Node* front = NULL;
struct Node* rear = NULL;


struct Node* create_node(int data) {
    struct Node* nd;
    nd = malloc(sizeof(struct Node));
    nd->data = data;
    nd->next = NULL;
    return nd;
}

void enqueue(int data) {
    struct Node* new_node = create_node(data);

    if (rear == NULL) {
        front = new_node;
        rear = new_node;
    } else {
        rear->next = new_node;
        rear = new_node;
    }
    printf("enqueued:%d\n", data);
}


int dequeue() {

    int data = front->data;
    struct Node* temp = front;
    front = front->next;

    if (front == NULL) {
        rear = NULL;
    }

    free(temp);
    printf("dequeue: %d\n", data);
    return data;
}


void displayQueue() {
    struct Node* temp = front;
    while (temp != NULL) {
        printf("%d -> ", temp->data);
        temp = temp->next;
    }
    printf("null\n");
}

int main(){
    enqueue(10);
    enqueue(20);
    enqueue(30);
    enqueue(40);

    printf("queue: ");
    displayQueue();
    dequeue();
    dequeue();
    displayQueue();
}