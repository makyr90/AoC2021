from common import get_input_of_day

def solve_part1(input_list):

    crab_pos = [int(x) for x in input_list[0].strip().split(",")]
    fuel_cost = []
    for pos in range(max(crab_pos)+1):
        fuel = [abs(x-pos) for x in crab_pos]
        fuel_cost.append(sum(fuel))

    return int(min(fuel_cost))

def solve_part2(input_list):

    crab_pos = [int(x) for x in input_list[0].strip().split(",")]
    fuel_cost = []
    for pos in range(max(crab_pos)+1):
        fuel = [(abs(x-pos)*((abs(x-pos)+1)/2)) for x in crab_pos]
        fuel_cost.append(sum(fuel))

    return int(min(fuel_cost))

if __name__ == '__main__':

    print("Day 7 part 1 answer: {}".format(solve_part1(get_input_of_day(7))))
    print("Day 7 part 2 answer: {}".format(solve_part2(get_input_of_day(7))))
