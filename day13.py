from common import get_input_of_day

def read_data(input_list):

    data_points = []
    folding_points = []
    for line in input_list:
        if "," in line:
            line = line.strip().split(",")
            x,y = int(line[1]),int(line[0])
            data_points.append([x,y])
        elif "=" in line:
            line=line.strip().split()[-1].split("=")
            if line[0]=="y":
                folding_points.append(["x",int(line[1])])
            elif line[0]=="x":
                folding_points.append(["y",int(line[1])])

    max_x = max(x[0] for x in data_points)+1
    max_y =  max(x[1] for x in data_points)+1
    data_grid = []
    for idx in range(max_x):
        row = ["."]*max_y
        data_grid.append(row)
    for dp in data_points:
        data_grid[dp[0]][dp[1]] = "#"

    return data_grid,folding_points

def count_dots(data_grid):

    return sum([x.count("#") for x in data_grid])

def horizindal_folding(data_grid,pos):

    upper_part = data_grid[:pos]
    bottom_part = data_grid[pos+1:]
    merged_grid = []
    for uprow,dowrow in zip(upper_part,reversed(bottom_part)):
        merged_row = []
        for x1,x2 in zip(uprow,dowrow):
            if x1=="#" or x2=="#":
                merged_row.append("#")
            else:
                merged_row.append(".")
        merged_grid.append(merged_row)

    return merged_grid

def verical_folding(data_grid,pos):

    left_part = [x[:pos] for x in data_grid]
    right_part = [x[pos+1:] for x in data_grid]
    merged_grid = []
    for lpart,rpart in zip(left_part,right_part):
        merged_row = []
        for y1,y2 in zip(reversed(lpart),rpart):
            if y1=="#" or y2=="#":
                merged_row.append("#")
            else:
                merged_row.append(".")
        merged_grid.append(merged_row)

    return merged_grid

def solve_part1(input_list):

    data_grid,folding_points = read_data(input_list)
    if folding_points[0][0]=="x":
        data_grid = horizindal_folding(data_grid,folding_points[0][1])
    elif folding_points[0][0]=="y":
        data_grid = verical_folding(data_grid,folding_points[0][1])

    return count_dots(data_grid)

def solve_part2(input_list):

    data_grid,folding_points = read_data(input_list)
    for folding_point in folding_points:
        if folding_point[0]=="x":
            data_grid = horizindal_folding(data_grid,folding_point[1])
        elif folding_point[0]=="y":
            data_grid = verical_folding(data_grid,folding_point[1])

    for row in data_grid:
        print(" ".join(reversed(row)))

if __name__ == '__main__':


    print("Day 13 part 1 answer: {}".format(solve_part1(get_input_of_day(13))))
    print("Day 13 part 2 answer:")
    solve_part2(get_input_of_day(13))
