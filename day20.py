from common import get_input_of_day

def read_data():

    data = get_input_of_day(20,True).split("\n\n")
    algo = data[0]
    image = dict()
    for idx,line in enumerate(data[1].split("\n")):
        line = line.strip()
        if line != "":
            for jdx,pixel in enumerate(line):
                pos = tuple([idx,jdx])
                image[pos] = pixel

    return algo, image

def image_enhancement(image,algo,infinite_on):

    image_copy = image.copy()
    for pos,pixel in image_copy.items():
        for idx in range(pos[0]-1,pos[0]+2):
            for jdx in range(pos[1]-1,pos[1]+2):
                if tuple([idx,jdx]) not in image:
                    image[tuple([idx,jdx])] = "#" if infinite_on else "."

    new_image = dict()
    for pos,pixel in image.items():
        digits = ""
        for idx in range(pos[0]-1,pos[0]+2):
            for jdx in range(pos[1]-1,pos[1]+2):
                if tuple([idx,jdx]) in image:
                    digits += "1" if image[tuple([idx,jdx])] == "#" else "0"
                else:
                    digits += "1" if infinite_on else "0"

        new_val = algo[int(digits,2)]
        new_image[pos] = new_val

    return new_image

def count_active_pixels(image):

    active_pixels = 0
    for pos,pixel in image.items():
        if pixel == "#":
            active_pixels += 1

    return active_pixels

def enhance_image(steps):

    algo, image = read_data()
    infinite_on = False
    for idx in range(steps):
        image = image_enhancement(image,algo,infinite_on)
        infinite_on = not infinite_on

    return count_active_pixels(image)

if __name__ == '__main__':

    print("Day 20 part 1 answer: {}".format(enhance_image(2)))
    print("Day 20 part 2 answer: {}".format(enhance_image(50)))
