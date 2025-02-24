
from collections import deque

graph = [
    [0, 1, 1, 1, 0],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 1, 0],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 1, 0]
]


# for i in graph:
#     for j in i:
#         print(j)
k = 0

adj_list = {i: [] for i in range(len(graph))}

for i in range(len(graph)):
    for j in range(len(graph[i])):

        # print(i,j,graph[i][j])
        
        if(graph[i][j] == 1):
            # print(i,j)
            
            
            adj_list[i].append(j)
            
            
            
def find_adjacent_nodes(adj):
    n = len(adj)  # Number of nodes
    adjacent_nodes = [[] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if adj[i][j] != 0:  # Check if there is an edge
                adjacent_nodes[i].append(j)
    
    return adjacent_nodes



adjacent_nodes = find_adjacent_nodes(graph)
# print(adj_list)
# print(adjacent_nodes)

start_node = 0
num_nodes = len(graph)
visited = [False]*num_nodes
queue = deque([start_node])
visited[start_node] = True
bfs_order = []

while queue:
    cur_node = queue.popleft()
    print(cur_node)
    bfs_order.append(cur_node)
    
    for neighbour in range(num_nodes):
        if graph[cur_node][neighbour] == 1 and visited[neighbour] == False:
            queue.append(neighbour)
            visited[neighbour] = True
            
            
    


            