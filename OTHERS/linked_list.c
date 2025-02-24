#include <stdlib.h>
#include <stdio.h>
#include <string.h>


struct Node{
    int data;
    struct Node* next;
};

struct Node nodearray[100];

struct Node* head = NULL;

int i = 0;

struct Node* create_node(int data){
    struct Node* new_node = &nodearray[i++];
    new_node->data = data;
    new_node->next = NULL;
    return new_node;
}

void appendNode(int data) {
    struct Node* newNode = create_node(data);   
    if (head == NULL) {
        head = newNode;
    } else {
        struct Node* temp = head;
        while (temp->next != NULL) {
            temp = temp->next;
        }
        temp->next = newNode;
    }
}


void displayList() {
    struct Node* temp = head;
    while (temp != NULL) {
        printf("%d -> ", temp->data);
        temp = temp->next;
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
    for(int i =0; i<100; i++){
        appendNode(i);
    }

    printf("Linked List: ");
    count();
    // pop();
    // pop();
    displayList();
}

