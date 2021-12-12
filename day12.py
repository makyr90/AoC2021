from common import get_input_of_day

def read_data(input_list):

    data = dict()
    for line in input_list:
        line = line.strip().split("-")
        head,tail = line[0],line[1]
        if head not in data:
            data[head] = [tail]
        else:
            if tail not in data[head]:
                data[head].append(tail)
        if tail not in data:
            data[tail] = [head]
        elif head not in data[tail]:
            data[tail].append(head)

    return data

def dfs(path,paths,small_caves_flag):

    if path[-1] == "end":
        paths.append(path)
    else:
        for neighbour in graph[path[-1]]:
            if not (neighbour.islower() and neighbour in path):
                new_path = path[:]
                new_path.append(neighbour)
                dfs(new_path,paths,small_caves_flag)
            elif small_caves_flag and path.count(neighbour)==1 and neighbour!="start":
                new_path = path[:]
                new_path.append(neighbour)
                dfs(new_path,paths,False)

    return len(paths)

if __name__ == '__main__':

    graph = read_data(get_input_of_day(12))
    print("Day 12 part 1 answer: {}".format(dfs(["start"],[],False)))
    print("Day 12 part 2 answer: {}".format(dfs(["start"],[],True)))
