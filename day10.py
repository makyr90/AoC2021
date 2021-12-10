from common import get_input_of_day

def solve_part1(input_list):

    scoring_dict = {")":3, "]":57, "}":1197, ">":25137}
    error_score = 0
    for line in input_list:
        line = line.strip()
        while (line!=""):
            line_lenght = len(line)
            # Remove direct open and closing brackets
            line = line.replace("()","").replace("[]","").replace("{}","").replace("<>","")
            if line_lenght == len(line):
                # Remove unclosed brackets
                line = line.replace("(","").replace("[","").replace("{","").replace("<","")
                break

        if line!="":
            error_score+= scoring_dict[list(line)[0]]

    return error_score

def solve_part2(input_list):

    scoring_dict = {"(":1, "[":2, "{":3, "<":4}
    line_scores = []
    for line in input_list:
        line = line.strip()
        while (line!=""):
            line_lenght = len(line)
            # Remove direct open and closing brackets
            line = line.replace("()","").replace("[]","").replace("{}","").replace("<>","")
            if line_lenght == len(line):
                #Remove corrupted lines
                line = line.replace(")","").replace("]","").replace("}","").replace(">","")
                if line_lenght!=len(line):
                    line = ""
                break

        if line!="":
            line_score = 0
            for elem in reversed(list(line)):
                line_score = (line_score*5) + scoring_dict[elem]
            line_scores.append(line_score)

    line_scores = sorted(line_scores)

    return line_scores[int(len(line_scores)/2)]

if __name__ == '__main__':

    print("Day 10 part 1 answer: {}".format(solve_part1(get_input_of_day(10))))
    print("Day 10 part 2 answer: {}".format(solve_part2(get_input_of_day(10))))
