from common import get_input_of_day

def solve_part1(input_list):

    horizontal_pos = 0
    depth = 0
    for line in input_list:
        line = line.split()
        direction = line[0].lower().strip()
        meters = int(line[1])
        if direction =="forward":
            horizontal_pos+=meters
        elif direction=="up":
            depth-=meters
        elif direction=="down":
            depth +=meters
        else:
            print("ERROR",direction)
    return horizontal_pos,depth

def solve_part2(input_list):

    horizontal_pos = 0
    depth = 0
    aim = 0
    for line in input_list:
        line = line.split()
        direction = line[0].lower().strip()
        meters = int(line[1])
        if direction =="forward":
            horizontal_pos+=meters
            depth+= (meters*aim)
        elif direction=="up":
            aim-=meters
        elif direction=="down":
            aim+=meters
        else:
            print("ERROR",direction)
    return horizontal_pos,depth


if __name__ == '__main__':

    horizontal_pos,depth = solve_part1(get_input_of_day(2))
    print("Day 2 part 1 answer: {}".format(horizontal_pos*depth))
    horizontal_pos,depth = solve_part2(get_input_of_day(2))
    print("Day 2 part 2 answer: {}".format(horizontal_pos*depth))
