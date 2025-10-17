grid = [
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0]
]


start = (0, 0)
target = (3, 3)
queue = []

def is_valid(x, y, m, n, grid, visited):
    return 0 <= x < m and 0 <= y < n and grid[x][y] == 0 and not visited[x][y]
    
    
def bfs(start,target,grid):
    sx,sy = start
    tx,ty = target
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False] * cols for i in range(rows)]
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    # print(visited)
    
    queue= []
    queue.append((sx,sy,0)) #(x,y,distance)tup
    visited[sx][sy] = True
    
    while queue:
        print(queue)
        x,y,dist = queue.pop(0)
        
        if((x,y) == (tx,ty)):
            return dist
        
        for dx,dy in directions:
            nx,ny = x+dx,y+dy
            if is_valid(nx, ny, rows, cols, grid, visited):
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))
    return -1
    
# print(bfs(start,target,grid))   

def find_paths(grid,targetX,targetY,visited):
    rows = len(grid)
    cols = len(grid[0])

    if()
    
    

    