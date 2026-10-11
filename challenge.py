from collections import deque

def bfs_grid(grid, start, cube, end):

    rows, cols = len(grid), len(grid[0])
    
    queue = deque([(start[0], start[1], [start])])
    
    visited = {start}
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    part1 = None

    while queue:
        
        r, c, path = queue.popleft()
        
        if (r, c) == cube:
            print('First goal reached, the cube is picked') 
            part1 = path
            break

     
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == 0 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc, path + [(nr, nc)]))
    
    if part1 is None: #the cube wasn't reached
        print('The cube is unreachable')
        return None
    
    queue_2 = deque([(cube[0], cube[1], [cube])])
    visited_2 = {cube}

    while queue_2:
        
        r, c, path = queue_2.popleft()
        
        if (r, c) == end:
            print('Second goal reached, the cube reached the final position')
            return part1 + path[1:]

            
        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == 0 and (nr, nc) not in visited_2:
                    visited_2.add((nr, nc))
                    queue_2.append((nr, nc, path + [(nr, nc)]))

    print('The goal is unreachable from the cube')             
    return None  # if no path exists


# 0 = Empty Cell, 1 = Obstacle

start_pos = (0, 0)
cube_pos = (2, 2)
end_pos = (4, 4)

example_grid_1 =[[0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0],
                [0, 0, 0, 1, 0]
                ]



print('Testing with grid 1:')
path_found = bfs_grid(example_grid_1, start_pos, cube_pos, end_pos)
print("Path:", path_found)


example_grid_2 =[[0, 1, 0, 0, 0],
                 [1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 0]
                 ]
print('Testing with grid 2:')
path_found = bfs_grid(example_grid_2, start_pos, cube_pos, end_pos)
print("Path:", path_found)


example_grid_3 =[[0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1],
                 [0, 0, 0, 1, 0]
                 ]
print('Testing with grid 3:')
path_found = bfs_grid(example_grid_3, start_pos, cube_pos, end_pos)
print("Path:", path_found)