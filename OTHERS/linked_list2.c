#include <stdlib.h>
#include <stdio.h>
#include <string.h>


struct Node{
    int data;
    struct Node* prev;
    struct Node* next;
};

struct Node* head = NULL;
struct Node* tail = NULL;

struct Node* create_node(int data){
    struct Node* nd;
    nd = malloc(sizeof (struct Node));
    nd->data = data;
    nd->prev = NULL;
    nd->next = NULL;
    return nd;
}

void appendNode(int data) {
    struct Node* new_node = create_node(data);

    if (head == NULL) {
        head = new_node;
        tail = new_node;
    } else {
        new_node->prev = tail;
        tail->next = new_node;
        tail = new_node;
    }
}


void insertNode(int pos, int data) {
    struct Node* new_node = create_node(data);
    struct Node* temp = head;

    for(int i=0; i<pos-1; i++){
        temp = temp->next;
    }
    new_node->next = temp->next; new_node->prev = temp;
    temp->next = new_node; new_node->next->prev = new_node;
}

void displayList() {
    struct Node* temp = head;
    while (temp != NULL) {
        printf("%d -> ", temp->data);
        temp = temp->next;
    }
    printf("NULL\n");
}

void displayListReverse() {
    struct Node* temp = tail;
    while (temp != NULL) {
        printf("%d -> ", temp->data);
        temp = temp->prev;
    }
    printf("NULL\n");
}

void count(){
    int ctr = 0;
    struct Node* temp = head;
    while(temp!=NULL){
        temp = temp->next;
        ctr++;
    }
    printf("Count: %d ",ctr);
}

void reverse_list(){
    struct Node* temp = tail;
    
    while(temp->prev!=NULL){
        tail->next = temp->prev;
        temp = temp->prev;
        tail = tail->next;
    }
}


// void pop(){

//      if (head->next == NULL) {
        
//         head = NULL;
//         printf("Last node removed.\n");
//         return;
//     }

    
//     struct Node* temp = head;
//      while (temp->next->next != NULL) {
//         temp = temp->next;
//         // ctr++;

//     }
//     temp->next = NULL;
//     printf("Last node removed.\n");
    
// }

int main(){
    // appendNode(1);
    // appendNode(2);
    // appendNode(3);
    // appendNode(55);
    for(int i =0; i<50; i++){
        appendNode(i);
    }

    // printf("Linked List: ");
    // count();
    // pop();
    // pop();
    // displayListReverse();

    insertNode(5, 500);
    displayList();
    printf("\n");
    // reverse_list();
    printf("\n");
    displayList();
    // displayListReverse();
}

