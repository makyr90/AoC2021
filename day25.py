from common import get_input_of_day
from copy import deepcopy

def read_data():

    lines = get_input_of_day(25)
    cucumbers = []
    for line in lines:
        cucumber_row = list(line.strip())
        cucumbers.append(cucumber_row)

    return cucumbers

def step_update(cucumbers):

    cucumbers_copy = deepcopy(cucumbers)
    movements = 0
    row_len = len(cucumbers[0])
    col_len = len(cucumbers)
    # update > first
    for idx in range(len(cucumbers)):
        for jdx in range(len(cucumbers[idx])):
            if cucumbers[idx][jdx] == ">" and cucumbers[idx][(jdx+1)%row_len] == ".":
                cucumbers_copy[idx][(jdx+1)%row_len] = ">"
                cucumbers_copy[idx][jdx] = "."
                movements += 1

    cucumbers = cucumbers_copy
    cucumbers_copy = deepcopy(cucumbers)
    # update v
    for idx in range(len(cucumbers)):
        for jdx in range(len(cucumbers[idx])):
            if cucumbers[idx][jdx] == "v" and cucumbers[(idx+1)%col_len][jdx] == ".":
                cucumbers_copy[(idx+1)%col_len][jdx] = "v"
                cucumbers_copy[idx][jdx] = "."
                movements += 1

    return cucumbers_copy, movements

def solve_part1():

    cucumbers = read_data()
    steps = 0
    while True:
        steps += 1
        cucumbers, movements = step_update(cucumbers)
        if movements == 0:
            break

    return steps

if __name__ == '__main__':

     print("Day 25 answer: {}".format(solve_part1()))
