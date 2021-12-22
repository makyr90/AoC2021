from common import get_input_of_day

def read_update_steps(clip=False):

    data = get_input_of_day(22)
    update_steps = []
    for line in data:
        val =  1 if line.strip().split()[0] == "on" else 0
        line = line.strip().split()[1].split(",")
        x_min, x_max = int(line[0].split("=")[1].split("..")[0]), int(line[0].split("=")[1].split("..")[1])
        y_min, y_max = int(line[1].split("=")[1].split("..")[0]), int(line[1].split("=")[1].split("..")[1])
        z_min, z_max = int(line[2].split("=")[1].split("..")[0]), int(line[2].split("=")[1].split("..")[1])
        if clip:
            if x_min < -50 or x_max > 50 or y_min < -50 or y_max > 50 or z_min < -50 or z_max > 50:
                continue
        dir_set = dict()
        dir_set["x"], dir_set["y"], dir_set["z"], dir_set["val"] = [x_min,x_max], [y_min,y_max], [z_min,z_max], val
        update_steps.append(dir_set)

    return update_steps

def axis_intersection(x,y):

    x1,x2 = x[0],x[1]
    y1,y2 = y[0],y[1]
    if y1 <= x1 <= y2 or y1 <= x2 <= y2 or x1 <= y1 <= x2 or x1 <= y2 <= x2:
        return True
    else:
        return False

def solve_part1():

    update_steps = read_update_steps(clip=True)
    cubes = dict()
    for step in update_steps:
        for x in range(step["x"][0],step["x"][1]+1):
            for y in range(step["y"][0],step["y"][1]+1):
                for z in range(step["z"][0],step["z"][1]+1):
                    cubes[(x,y,z)] = step["val"]

    return sum(cubes.values())

def solve_part2():

    update_steps = read_update_steps(clip=False)
    disjoint_cubes = []
    for cube in update_steps:
        x1,x2 = cube["x"]
        y1,y2 = cube["y"]
        z1,z2 = cube["z"]
        value = cube["val"]
        x2,y2,z2 = x2+1,y2+1,z2+1
        new_cube = [x1,x2,y1,y2,z1,z2,value]

        iter_disjoint_cubes = []
        for elem in disjoint_cubes:
            x_axis_intersection = axis_intersection((x1,x2),(elem[0],elem[1]))
            y_axis_intersection = axis_intersection((y1,y2),(elem[2],elem[3]))
            z_axis_intersection = axis_intersection((z1,z2),(elem[4],elem[5]))

            if x_axis_intersection and y_axis_intersection and z_axis_intersection:

                # left
                if elem[0] < x1:
                    l_cube = [elem[0],x1,elem[2],elem[3],elem[4],elem[5],elem[6]]
                    iter_disjoint_cubes.append(l_cube)
                    elem[0] = x1
                # right
                if elem[1] > x2:
                    r_cube = [x2,elem[1],elem[2],elem[3],elem[4],elem[5],elem[6]]
                    iter_disjoint_cubes.append(r_cube)
                    elem[1] = x2
                # up
                if elem[2] < y1:
                    u_cube = [elem[0],elem[1],elem[2],y1,elem[4],elem[5],elem[6]]
                    iter_disjoint_cubes.append(u_cube)
                    elem[2] = y1
                # down
                if elem[3] > y2:
                    d_cube = [elem[0],elem[1],y2,elem[3],elem[4],elem[5],elem[6]]
                    iter_disjoint_cubes.append(d_cube)
                    elem[3] = y2
                # back
                if elem[4] < z1:
                    b_cube = [elem[0],elem[1],elem[2],elem[3],elem[4],z1,elem[6]]
                    iter_disjoint_cubes.append(b_cube)
                    elem[4] = z1
                # front
                if elem[5] > z2:
                    f_cube = [elem[0],elem[1],elem[2],elem[3],z2,elem[5],elem[6]]
                    iter_disjoint_cubes.append(f_cube)
                    elem[5] = z2
            else:
                iter_disjoint_cubes.append(elem)

        iter_disjoint_cubes.append(new_cube)
        disjoint_cubes = iter_disjoint_cubes

    on_cubes = 0
    for cube in disjoint_cubes:
        if cube[6] == 1:
            on_cubes += ((abs(cube[1]-cube[0]))*(abs(cube[3]-cube[2]))*(abs(cube[5]-cube[4])))

    return on_cubes

if __name__ == '__main__':

    print("Day 22 part 1 answer: {}".format(solve_part1()))
    print("Day 22 part 2 answer: {}".format(solve_part2()))
