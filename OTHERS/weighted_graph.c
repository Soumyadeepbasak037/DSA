#include <stdio.h>
#include <stdlib.h>

struct edge{
    int destination;
    int weight;
    struct edge* next;
};

struct node{
    int vertex;
    struct edge* head;
};

struct graph{
    int num_vertices;
    int num_edges;
    struct node* adjacencylist[];
};

struct edge* create_edge(int destination,int weight){
    struct edge* new_edge = malloc(sizeof(struct edge));
    new_edge->destination = destination;
    new_edge->weight = weight;
    new_edge->next = NULL;
    return new_edge;
}

struct graph* create_graph(int num_vetrices, int num_edges){


}


