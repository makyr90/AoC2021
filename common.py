import os

def get_input_of_day(day_number,raw=False):

    with open("data"+os.sep+"day"+str(day_number)+".txt") as f:
        if raw:
            return f.read()
        lines = f.readlines()
        input_list = []
        for line in lines:
            input_list.append(line)

    return input_list
