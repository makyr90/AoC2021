from common import get_input_of_day
from itertools import permutations, product

def read_input(input):
    scanners = []
    data = input.split("\n\n")
    for scanner in data:
        beacons = []
        for beacon in scanner.split("\n")[1:]:
            if beacon.strip() != "":
                beacons.append([int(x) for x in beacon.split(",")])
        scanners.append(beacons)

    return scanners

def get_all_possible_orientations(scanner):

    for perm in permutations((0,1,2)):
        for sign_x,sign_y,sign_z in product((-1, 1), repeat=3):
            yield [[x[perm[0]]*sign_x,x[perm[1]]*sign_y,x[perm[2]]*sign_z] for x in scanner]

def get_all_pair_distances(scanner1,scanner2):

    for oriented_scanner2 in get_all_possible_orientations(scanner2):
        distances = dict()
        for beacon1,beacon2 in product(scanner1,oriented_scanner2):
            dist = tuple([beacon2[0]-beacon1[0],beacon2[1]-beacon1[1],beacon2[2]-beacon1[2]])
            if dist not in distances:
                distances[dist] = 1
            else:
                distances[dist] += 1
        for k,v in distances.items():
            if v >= 12:
                distance = k
                overlapped_beacons = [tuple([x[0]-k[0],x[1]-k[1],x[2]-k[2]]) for x in oriented_scanner2]

                return True, distance, overlapped_beacons

    return False, None, None

def manhattan_distance(pos1,pos2):

    return sum(abs(x-y) for x,y in zip(pos1,pos2))

def get_largest_distance(scanner_pos):

    scanner_pos = list(scanner_pos)
    all_pair_distances = []
    for idx in range(len(scanner_pos)-1):
        for jdx in range(idx+1,len(scanner_pos)):
            all_pair_distances.append(manhattan_distance(scanner_pos[idx],scanner_pos[jdx]))

    return max(all_pair_distances)

def solve_parts1_2():

    scanners = read_input(get_input_of_day(19,True))
    all_beacons = set()
    all_beacons.update([tuple([x[0],x[1],x[2]]) for x in scanners[0]])
    scanner_indexes = {x for x in range(len(scanners))}
    solved_indexes, scanner_pos = set(), set()
    solved_indexes.add(0)
    scanner_pos.add(tuple([0,0,0]))

    while len(solved_indexes)!=len(scanners):
        for scanner_index in scanner_indexes.difference(solved_indexes):
            overlap_flag, distance, beacons = get_all_pair_distances(all_beacons,scanners[scanner_index])
            if overlap_flag:
                solved_indexes.add(scanner_index)
                scanner_pos.add(distance)
                all_beacons.update(beacons)

    return len(all_beacons), get_largest_distance(scanner_pos)

if __name__ == '__main__':

    part1_answer, part2_answer = solve_parts1_2()
    print("Day 19 part 1 answer: {}".format(part1_answer))
    print("Day 19 part 2 answer: {}".format(part2_answer))
