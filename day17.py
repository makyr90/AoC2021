from common import get_input_of_day

def check_probe(x,y,vx,vy):
    
    pos = [0,0]
    max_depth = 0
    while True:
        if x[0] <= pos[0] <= x[1] and y[0] <= pos[1] <= y[1]:
            return max_depth
        if pos[0] > x[1] or pos[1] < y[0]:
            return 0
        pos[0]+=vx
        pos[1]+=vy
        vy-=1
        vx = vx-1 if vx > 0 else 0
        max_depth = max(max_depth,abs(pos[1]))

def bf_initial_velocity():

    data = get_input_of_day(17)[0].strip().split(":")[1].strip().split(",")
    x = [int(x) for x in data[0].split("=")[1].split("..")]
    y = [int(y) for y in data[1].split("=")[1].split("..")]
    all_valid_inits = []
    for vx in range(0,x[1]+1):
        for vy in range(y[0]-1,-(y[0]-1)):
            perm_depth = check_probe(x,y,vx,vy)
            if perm_depth!=0:
                all_valid_inits.append(perm_depth)

    return max(all_valid_inits),len(all_valid_inits)

if __name__ == '__main__':

    max_depth,valid_inits = bf_initial_velocity()
    print("Day 17 part 1 answer: {}".format(max_depth))
    print("Day 17 part 2 answer: {}".format(valid_inits))
