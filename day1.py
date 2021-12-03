from common import get_input_of_day

def solve_part1(input_list):

    input = [int(x.strip()) for x in input_list]
    counter = 0
    for idx in range(1,len(input)):
        if input[idx] > input[idx-1]:
            counter+=1
    return(counter)

def solve_part2(input_list):

    input = [int(x.strip()) for x in input_list]
    triplet_sums = []
    for idx in range(len(input)-2):
        sum = input[idx] + input[idx+1] + input[idx+2]
        triplet_sums.append(sum)

    counter = 0
    for idx in range(1,len(triplet_sums)):
        if triplet_sums[idx] > triplet_sums[idx-1]:
            counter+=1
    return counter

if __name__ == '__main__':

    print("Day 1 part 1 answer: {}".format(solve_part1(get_input_of_day(1))))
    print("Day 1 part 2 answer: {}".format(solve_part2(get_input_of_day(1))))
