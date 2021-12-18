from common import get_input_of_day
import math

def parse_number(line):

    number_pairs = []
    depth = 0
    index = 0
    line = line.strip()
    while index < len(line):
        if line[index] == "[":
            depth += 1
            index += 1
        elif line[index] == "]":
            depth -= 1
            index += 1
        else:
            if line[index] != ",":
                digits = ""
                while line[index].isdigit():
                    digits += line[index]
                    index += 1
                number_pairs.append([int(digits),depth])
            else:
                index += 1
    return number_pairs

def merge_lines(line_1,line_2):

    return [[x[0],x[1]+1] for x in line_1+line_2]

def explode(number_pairs):

    for idx,pair in enumerate(number_pairs):
        if pair[1] >= 5:
            assert idx < len(number_pairs) -1, "Parsing error, not valid pair"
            assert number_pairs[idx][1] == number_pairs[idx+1][1],"Depth error"
            if idx > 0:
                number_pairs[idx-1][0] += pair[0]
            if idx < len(number_pairs)-2:
                number_pairs[idx+2][0] += number_pairs[idx+1][0]

            number_pairs[idx:idx+2] = [[0,pair[1]-1]]
            return True, number_pairs

    return False , number_pairs

def split(number_pairs):

    for idx,pair in enumerate(number_pairs):
        if pair[0] >= 10:
            left_part = [math.floor(pair[0]/2),pair[1]+1]
            right_part = [math.ceil(pair[0]/2),pair[1]+1]
            number_pairs[idx:idx+1] = [left_part, right_part]
            return True, number_pairs

    return False , number_pairs

def reduce(number_pairs):

    while True:
        explosion_flag, number_pairs = explode(number_pairs)
        if explosion_flag:
            continue
        split_flag, number_pairs = split(number_pairs)
        if split_flag:
            continue
        break

    return number_pairs

def magnitude(number_pairs):

    while len(number_pairs) > 1:
        magnitude_pairs = []
        index = 0
        while index < len(number_pairs)-1:
            if number_pairs[index][1] == number_pairs[index+1][1]:
                magnitude_pairs.append([3*number_pairs[index][0]+2*number_pairs[index+1][0],number_pairs[index][1]-1])
                index += 2
            else:
                magnitude_pairs.append(number_pairs[index])
                index += 1
        if index == len(number_pairs):
            magnitude_pairs.append(number_pairs[index-1])

        number_pairs = magnitude_pairs

    return number_pairs[0][0]

def solve_part1(data):

    line = parse_number(data[0])
    for l in data[1:]:
        line = merge_lines(line,parse_number(l))
        line = reduce(line)

    return magnitude(line)

def solve_part2(data):

    all_magnitutes = []
    for idx in range(len(data)-1):
        for jdx in range(idx+1,len(data)):
            l1 = parse_number(data[idx])
            l2 = parse_number(data[jdx])
            line = merge_lines(l1,l2)
            line_r = merge_lines(l2,l1)
            all_magnitutes.append(magnitude(reduce(line)))
            all_magnitutes.append(magnitude(reduce(line_r)))

    return max(all_magnitutes)

if __name__ == '__main__':

    data = get_input_of_day(18)
    print("Day 18 part 1 answer: {}".format(solve_part1(data)))
    print("Day 18 part 2 answer: {}".format(solve_part2(data)))
