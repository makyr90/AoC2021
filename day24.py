from common import get_input_of_day

# if x > 0:  Z_i = Z_i-1 * 26 + input_i + y_i   7 cases
# if x < 0:  Z_i = Z_i-1 div 26  7 cases.
# For these cases we must ensure that z % 26 + x = w to end up with z = 0
# z % 26 is actually the last y+w value when a x > 0 was encountered.
# y_max = 15 and w_max = 9. Thus y_max + w_max = 24 < 26
# Thus, we must ensure in x < 0 cases that w_i = w_i-1 + y_i-1 + x_i, where i-1
# is the latest block we encountered x > 0.
# Thus when x < 0 w_i must be  x_i + y_i-1 away from w_i-1

def read_data():

    lines = get_input_of_day(24)
    xy_pairs = []
    for idx in range(len(lines)):
        line = lines[idx].strip()
        if " ".join(line.split()[:2]) == "div z":
            x = int(lines[idx+1].split()[2])
            y = int(lines[idx+11].split()[2])
            xy_pairs.append((x,y))

    return xy_pairs

def get_pos_constraints(xy_pairs):

    pos_constaints = dict()
    input_history = []
    for index,pair in enumerate(xy_pairs):
        if pair[0] > 0:
            input_history.append((index,pair[1]))
        else:
            last_xpos_history = input_history.pop()
            pos_constaints[index] = [last_xpos_history[0],last_xpos_history[1]+pair[0]]

    assert len(input_history) == 0, "Error during pos constraints calculation"

    return pos_constaints

def get_max_monad(pos_constaints):

    digits = [9]*14
    for k,v in pos_constaints.items():
        digits[k] = min(9,9+v[1])
        digits[v[0]] = min(9,9-v[1])

    return int("".join([str(x) for x in digits]))

def get_min_monad(pos_constaints):

    digits = [1]*14
    for k,v in pos_constaints.items():
        digits[k] = max(1,1+v[1])
        digits[v[0]] = max(1,1-v[1])

    return int("".join([str(x) for x in digits]))

if __name__ == '__main__':

    pos_constaints = get_pos_constraints(read_data())
    print("Day 24 part 1 answer: {}".format(get_max_monad(pos_constaints)))
    print("Day 24 part 2 answer: {}".format(get_min_monad(pos_constaints)))
