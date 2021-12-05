from common import get_input_of_day

def count_overlapped_lines(data_points,value=2):

    counter = 0
    for k,v in data_points.items():
        if v>=value:
            counter+=1
    return counter

def update_dict(data_points,key):

    if key not in data_points:
        data_points[key] = 1
    else:
        data_points[key] +=1

    return data_points

def find_hydrothermal_vents(input_list,include_diagonals=False):

    data_points = dict()
    for line in input_list:
        # Get data points
        start, end = [x.split(',') for x in line.split(' -> ')]
        x1, y1 = int(start[0]), int(start[1])
        x2, y2 = int(end[0]), int(end[1])
        # horizontal and vertical lines
        if x1==x2 or y1==y2:
            for xidx in range(min(x1,x2),max(x1,x2)+1):
                for yidx in range(min(y1,y2),max(y1,y2)+1):
                    data_points = update_dict(data_points,str(xidx)+"|"+str(yidx))

        # diagonal lines
        elif include_diagonals and abs(x1-x2)==abs(y1-y2):
            for xidx in range(min(x1,x2),max(x1,x2)+1):
                for yidx in range(min(y1,y2),max(y1,y2)+1):
                    # consider only points of the defined diagonal
                    if  abs(xidx-x2)==abs(yidx-y2):
                        data_points = update_dict(data_points,str(xidx)+"|"+str(yidx))

    return count_overlapped_lines(data_points)

if __name__ == '__main__':

    print("Day 5 part 1 answer: {}".format(find_hydrothermal_vents(get_input_of_day(5))))
    print("Day 5 part 2 answer: {}".format(find_hydrothermal_vents(get_input_of_day(5),True)))
