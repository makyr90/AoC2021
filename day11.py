from common import get_input_of_day

def read_data(input_list):

    data = dict()
    for idx,line in enumerate(input_list):
        line = list(line.strip())
        for jdx,elem in enumerate(list(line)):
            pos = str(idx)+str(jdx)
            data[pos] = int(elem)

    return data

def check_flash(data):

    for k,v in data.items():
        if v > 9:
            return True,k
    return False,None

def step_update(data,increment_val=1):

    return {key:val+increment_val for key,val in data.items()}

def update_flash(data,pos,flashed_indexes,increment_val=1):

    data[pos] = 0
    x,y = int(list(pos)[0]),int(list(pos)[1])
    adjacent_indexes = [ str(x-1)+str(y-1), str(x-1)+str(y+1), str(x+1)+str(y-1), str(x+1)+str(y+1),
    str(x)+str(y+1), str(x)+str(y-1), str(x+1)+str(y), str(x-1)+str(y)]
    for adjacent_index in adjacent_indexes:
        if adjacent_index in data and adjacent_index not in flashed_indexes:
            data[adjacent_index]+=increment_val

    return data

def all_flash(data):

    for k,v in data.items():
        if v!=0:
            return False
    return True

def solve_parts1_2(input_list,steps=1000000000):

    octopus_energy = read_data(input_list)
    flash_counter = 0
    all_flash_step = None
    for step in range(steps):
        if all_flash(octopus_energy):
            all_flash_step = step
            break
        octopus_energy = step_update(octopus_energy)
        flashed_indexes = []
        flash_check,index = check_flash(octopus_energy)
        while flash_check:
            if index not in flashed_indexes:
                flashed_indexes.append(index)
                if step < 100:
                    flash_counter+=1
                octopus_energy=update_flash(octopus_energy,index,flashed_indexes)
                flash_check,index = check_flash(octopus_energy)

    return flash_counter,all_flash_step

if __name__ == '__main__':

    total_flashes, all_flash_step = solve_parts1_2(get_input_of_day(11))
    print("Day 11 part 1 answer: {}".format(total_flashes))
    print("Day 11 part 2 answer: {}".format(all_flash_step))
