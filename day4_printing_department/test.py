def get_neighbour_rolls(grid, x, y):
    neighbours = 0
    nx = x - 1
    for i1 in range(3):
        ny = y - 1
        for i2 in range(3):
            print(grid[nx][ny])
            if (nx != x or ny != y) and (nx >= 0 and nx < len(grid)) and (ny >= 0 and ny < len(grid[0])):
                n = grid[nx][ny]
                if n == '@':
                    neighbours += 1
                
            ny += 1
        nx += 1
    return neighbours

grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

get_neighbour_rolls(grid, 1, 1)


