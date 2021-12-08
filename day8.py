from common import get_input_of_day
import itertools

segments_numbers_mapping = dict()
segments_numbers_mapping["".join(["a","b","c","e","f","g"])] = 0
segments_numbers_mapping["".join(["c","f"])] = 1
segments_numbers_mapping["".join(["a","c","d","e","g"])] = 2
segments_numbers_mapping["".join(["a","c","d","f","g"])] = 3
segments_numbers_mapping["".join(["b","c","d","f"])] = 4
segments_numbers_mapping["".join(["a","b","d","f","g"])] = 5
segments_numbers_mapping["".join(["a","b","d","e","f","g"])] = 6
segments_numbers_mapping["".join(["a","c","f"])] = 7
segments_numbers_mapping["".join(["a","b","c","d","e","f","g"])] = 8
segments_numbers_mapping["".join(["a","b","c","d","f","g"])] = 9

def get_all_possible_mapping_permutations():

    possible_mapping_permutations = []
    segments_list = ["a","b","c","d","e","f","g"]
    for perm in list(itertools.permutations(segments_list)):
        perm_dict = dict()
        for idx,elem in enumerate(perm):
            perm_dict[segments_list[idx]] = elem
        possible_mapping_permutations.append(perm_dict)

    return possible_mapping_permutations

def valid_permutated_number(input_string,permutation_dict):

    permutated_string = []
    for letter in list(input_string):
        permutated_string.append(permutation_dict[letter])
    if "".join(sorted(permutated_string)) in segments_numbers_mapping:
        return True
    else:
        return False

def calculate_output_digits(input_strings,permutation_dict):

    valid_digits = []
    for elem in input_strings:
        valid_elem = []
        for letter in list(elem):
            valid_elem.append(permutation_dict[letter])
        valid_digits.append(str(segments_numbers_mapping["".join(sorted(valid_elem))]))

    return int("".join(valid_digits))

def solve_part1(input_list):

    unique_segments_counter = 0
    for line in input_list:
        output_vals = line.split("|")[1].split()
        for val in output_vals:
            if len(set(list(val))) in [2,3,4,7]:
                unique_segments_counter+=1

    return unique_segments_counter

def solve_part2(input_list):

    output_sum = 0
    possible_mapping_permutations = get_all_possible_mapping_permutations()
    valid_mapping_schema = None
    for line in input_list:
        signals = line.split("|")[0].split()
        digits = line.split("|")[1].split()
        all_vals = signals + digits
        for perm in possible_mapping_permutations:
            valid_perm = True
            for val in all_vals:
                if not valid_permutated_number(val,perm):
                    valid_perm = False
            if valid_perm:
                valid_mapping_schema = perm
                output_value = calculate_output_digits(digits,valid_mapping_schema)
                output_sum+=output_value
                break

        if valid_perm == False:
            print("ERROR")

    return output_sum

if __name__ == '__main__':

    print("Day 8 part 1 answer: {}".format(solve_part1(get_input_of_day(8))))
    print("Day 8 part 2 answer: {}".format(solve_part2(get_input_of_day(8))))
