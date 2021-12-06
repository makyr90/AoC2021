from common import get_input_of_day

def count_lanternfishs(input_list,days):

    lanterfishes = dict()
    for idx in range(0,9):
        lanterfishes[idx] = 0
    for line in input_list:
        fishes_timers = line.strip().split(",")
        for fish_timer in fishes_timers:
            lanterfishes[int(fish_timer)] +=1

    for day in range(days):
        lanterfishes_copy = lanterfishes.copy()
        for k,v in lanterfishes_copy.items():
            if k-1==-1:
                lanterfishes[0] = 0
                lanterfishes[6] += v
                lanterfishes[8] += v
            else:
                k = k -1
                lanterfishes[k]+=v
                lanterfishes[k+1] -= v

    return sum(lanterfishes.values())

if __name__ == '__main__':

    print("Day 6 part 1 answer: {}".format(count_lanternfishs(get_input_of_day(6),80)))
    print("Day 6 part 2 answer: {}".format(count_lanternfishs(get_input_of_day(6),256)))
