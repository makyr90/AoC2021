from common import get_input_of_day
from collections import defaultdict

def read_data(input_list):

    rules = dict()
    sequence = None
    for line in input_list:
        line = line.strip()
        if "->" in line:
            line = line.split(" -> ")
            rules[line[0]] = [list(line[0])[0] + line[1], line[1]+ list(line[0])[1]]
        else:
            if line!="":
                sequence = line

    return sequence,rules

def initial_bigrams(sequence):

    bigrams = defaultdict(int)
    sequence = list(sequence)
    for idx in range(len(sequence)-1):
        bigram = "".join([sequence[idx],sequence[idx+1]])
        bigrams[bigram] += 1

    return bigrams

def solve_parts1_2(input_list,steps):

    sequence,rules = read_data(input_list)
    letters_counter = defaultdict(int)
    for letter in list(sequence):
        letters_counter[letter]+=1
    iter_bigrams_counter = initial_bigrams(sequence)
    for idx in range(steps):
        for k,v in iter_bigrams_counter.copy().items():
            iter_bigrams_counter[k]-=v
            for elem in rules[k]:
                iter_bigrams_counter[elem]+=v
            letters_counter[list(rules[k][0])[1]]+=v

    return max(letters_counter.values())-min(letters_counter.values())

if __name__ == '__main__':

    print("Day 14 part 1 answer: {}".format(solve_parts1_2(get_input_of_day(14),10)))
    print("Day 14 part 1 answer: {}".format(solve_parts1_2(get_input_of_day(14),40)))
