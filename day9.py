from common import get_input_of_day

def read_data(input_list):

    input_nums = dict()
    for idx,line in enumerate(input_list):
        nums = [int(x) for x in list(line.strip())]
        for jdx,num in enumerate(nums):
            pos = str(idx)+"|"+str(jdx)
            input_nums[pos] = num

    return input_nums

def get_adjacent_points(index,data):

    row_index = int(index.split("|")[0])
    col_index = int(index.split("|")[1])
    adjacent_points = []
    adjacent_indexes = []
    if str(row_index+1)+"|"+str(col_index) in data:
        adjacent_points.append(data[str(row_index+1)+"|"+str(col_index)])
        adjacent_indexes.append(str(row_index+1)+"|"+str(col_index))
    if str(row_index-1)+"|"+str(col_index) in data:
        adjacent_points.append(data[str(row_index-1)+"|"+str(col_index)])
        adjacent_indexes.append(str(row_index-1)+"|"+str(col_index))
    if str(row_index)+"|"+str(col_index+1) in data:
        adjacent_points.append(data[str(row_index)+"|"+str(col_index+1)])
        adjacent_indexes.append(str(row_index)+"|"+str(col_index+1))
    if str(row_index)+"|"+str(col_index-1) in data:
        adjacent_points.append(data[str(row_index)+"|"+str(col_index-1)])
        adjacent_indexes.append(str(row_index)+"|"+str(col_index-1))

    return adjacent_points,adjacent_indexes

def get_lowest_points(data):

    lowest_points = []
    lowest_point_indexes = []
    input_nums_copy = data.copy()
    for k,v in input_nums_copy.items():
        adjacent_points,indexes = get_adjacent_points(k,data)
        if all(v<x for x in adjacent_points):
            lowest_points.append(v)
            lowest_point_indexes.append(k)

    return lowest_points,lowest_point_indexes

def get_basin_elements(index,data):

    visited = []
    queue = []
    visited.append(index)
    queue.append(index)
    while queue:
        s = queue.pop(0)
        val = data[s]
        adjacent_points,indexes = get_adjacent_points(s,data)
        for neighbour,ind in zip(adjacent_points,indexes):
            if neighbour > val and neighbour!=9:
                if ind not in visited:
                    visited.append(ind)
                    queue.append(ind)

    return visited

def solve_part1(input_list):

    input_nums = read_data(input_list)
    lowest_points,indexes = get_lowest_points(input_nums)

    return sum(lowest_points)+len(lowest_points)

def solve_part2(input_list):

    input_nums = read_data(input_list)
    lowest_points,indexes = get_lowest_points(input_nums)
    basin_sizes = []
    for l_point in indexes:
        basin_sizes.append(len(get_basin_elements(l_point,input_nums)))
    basin_sizes.sort(reverse=True)

    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]

if __name__ == '__main__':

    print("Day 9 part 1 answer: {}".format(solve_part1(get_input_of_day(9))))
    print("Day 9 part 2 answer: {}".format(solve_part2(get_input_of_day(9))))
