from common import get_input_of_day
from itertools import chain

def get_neighbours(pos,grid):

    x,y = pos[0],pos[1]
    neighbours = []
    if x > 0:
        neighbours.append((x-1,y))
    if x < len(grid)-1:
        neighbours.append((x+1,y))
    if y > 0:
        neighbours.append((x,y-1))
    if y < len(grid[0])-1:
        neighbours.append((x,y+1))

    return neighbours

def expand_grid(grid):

    expanded_grid = []
    for row in grid:
        expanded_row = [row]
        for idx in range(4):
            right_expansion = [int(x)+1 if int(x)<9 else 1 for x in expanded_row[-1]]
            expanded_row.append(right_expansion)
        expanded_grid.append(list(chain(*expanded_row)))

    expanded_grid_copy = expanded_grid[:]
    for idx in range(4):
        bottom_grid = []
        for row in expanded_grid_copy:
            new_row = [int(x)+1 if int(x)<9 else 1 for x in row]
            bottom_grid.append(new_row)
            expanded_grid.append(new_row)
        expanded_grid_copy = bottom_grid

    return expanded_grid

def min_cost(grid):

    adjacency_cost = [[float("inf") for _ in range(len(grid[0]))] for _ in range(len(grid))]
    adjacency_cost[0][0] = 0
    path_nodes = [(0,0)]
    while len(path_nodes) > 0:
        current_node = path_nodes.pop(0)
        current_cost = adjacency_cost[current_node[0]][current_node[1]]
        for neighbour in get_neighbours(current_node,grid):
            neighbour_cost = adjacency_cost[neighbour[0]][neighbour[1]]
            path_cost = current_cost + grid[neighbour[0]][neighbour[1]]
            if path_cost < neighbour_cost:
                adjacency_cost[neighbour[0]][neighbour[1]] = path_cost
                path_nodes.append(neighbour)

    return adjacency_cost[-1][-1]

if __name__ == '__main__':

    data = get_input_of_day(15)
    grid = [[int(x) for x in list(line.strip())] for line in data]
    expanded_grid = expand_grid(grid)
    print("Day 15 part 1 answer: {}".format(min_cost(grid)))
    print("Day 15 part 2 answer: {}".format(min_cost(expanded_grid)))
