#include <stdio.h>
#include <stdlib.h>

#define MAX_VERTICES 100


void initializeMatrix(int matrix[MAX_VERTICES][MAX_VERTICES], int numVertices) {
    int i, j;
    for (i = 0; i < numVertices; i++) {
        for (j = 0; j < numVertices; j++) {
            matrix[i][j] = 0;
        }
    }
}

void addEdge(int matrix[MAX_VERTICES][MAX_VERTICES], int startVertex, int endVertex, int weight) {
    matrix[startVertex][endVertex] = weight;
    matrix[endVertex][startVertex] = weight; //undirected graph
    
}


// void printMatrix(int matrix[MAX_VERTICES][MAX_VERTICES], int numVertices) {
//     int i, j;
//     printf("Adjacency Matrix:\n");
//     for (i = 0; i < numVertices; i++) {
//         for (j = 0; j < numVertices; j++) {
//             printf("%d ", matrix[i][j]);
//         }
//         printf("\n");
//     }
// }


void printMatrix(int matrix[MAX_VERTICES][MAX_VERTICES], int numVertices) {
    int i, j;
    printf("Adjacency Matrix (Weights):\n");
    for (i = 0; i < numVertices; i++) {
        for (j = 0; j < numVertices; j++) {
            if (matrix[i][j] == 0) {
                printf("0 "); // No edge
            } else {
                printf("%d ", matrix[i][j]); // Weght of edg
            }
        }
        printf("\n");
    }
}

void neighbours(int node, int matrix[MAX_VERTICES][MAX_VERTICES], int numVertices){
    int i,j;
    for(i=0; i<numVertices; i++){
        for(j=0 ; j<numVertices; j++){
            if(j==1){
                printf("%d",j);
            }
        }
    }

}




int main() {
     int numVertices, numEdges;
    int startVertex, endVertex, weight;
    int adjacencyMatrix[MAX_VERTICES][MAX_VERTICES];

    printf("Enter number of vertices: ");
    scanf("%d", &numVertices);
    printf("Enter number of edges: ");
    scanf("%d", &numEdges);

    initializeMatrix(adjacencyMatrix, numVertices);

    printf("Enter edges (startVertex endVertex weight):\n");
    for (int i = 0; i < numEdges; i++) {
        scanf("%d %d %d", &startVertex, &endVertex, &weight);
        addEdge(adjacencyMatrix, startVertex, endVertex, weight);
    }

    printMatrix(adjacencyMatrix, numVertices);
    
    





    // matrix_to_list(adjacencyMatrix,numVertices);


    // int adjlist[numVertices];

    // int k = 0;

    // for(int i =0; i<numVertices; i++){
    //     for(int j =0; j<numVertices; j++){
    //         if(adjacencyMatrix[i][j] != 0){
    //             adjlist[i] = j;
    //         }
    //     }
    // }
}


