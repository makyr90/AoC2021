from common import get_input_of_day

def hex_to_bit(num):

    num = bin(int(num,16))[2:]
    if len(num) < 4:
        num = "0" * (4 -len(num)) + num

    return num

def hex_to_bit_sequnece(input_data):

    input_data = input_data[0].strip()
    bits_sequence = []
    for hex in input_data:
        bits_sequence.append(hex_to_bit(hex))

    return "".join(bits_sequence)

def parse_packets(bits_sequence):

    version = int(bits_sequence[0:3],2)
    type_id = int(bits_sequence[3:6],2)
    packets_tree = dict()
    packets_tree["version"] = version
    packets_tree["id"] = type_id
    packets_tree["subpackets"] = []
    # Base case
    if packets_tree["id"] == 4:
        bits_sequence = bits_sequence[6:]
        binary_num = ""
        while bits_sequence[0] == "1":
            binary_num+= bits_sequence[1:5]
            bits_sequence = bits_sequence[5:]
        binary_num+= bits_sequence[1:5]
        bits_sequence = bits_sequence[5:]
        packets_tree["literal_value"] = int(binary_num,2)
        return packets_tree, bits_sequence

    else:
        length_id = bits_sequence[6]
        if length_id == "0":
            subpackets_length = int(bits_sequence[7:22],2)
            bits_subpackets = bits_sequence[22:22+subpackets_length]
            bits_sequence = bits_sequence[22+subpackets_length:]
            while len(bits_subpackets) > 0:
                 subpacket, bits_subpackets = parse_packets(bits_subpackets)
                 packets_tree["subpackets"].append(subpacket)
        else:
            n_subpackets = int(bits_sequence[7:18],2)
            bits_sequence = bits_sequence[18:]
            for packt in range(n_subpackets):
                subpacket, bits_sequence = parse_packets(bits_sequence)
                packets_tree["subpackets"].append(subpacket)

        return packets_tree, bits_sequence

def sum_versions(packets_hierarchy):

    return sum(sum_versions(subpacket) for subpacket in packets_hierarchy["subpackets"]) + packets_hierarchy["version"]

def decode_value(packets_hierarchy):

    if packets_hierarchy["id"] == 0:
        return sum(decode_value(subpacket) for subpacket in packets_hierarchy["subpackets"])
    elif packets_hierarchy["id"] == 1:
        val =  1
        subvalues = [decode_value(subpacket) for subpacket in packets_hierarchy["subpackets"]]
        for subvalue in subvalues:
            val*=subvalue
        return val
    elif packets_hierarchy["id"] == 2:
        return min(decode_value(subpacket) for subpacket in packets_hierarchy["subpackets"])
    elif packets_hierarchy["id"] == 3:
        return max(decode_value(subpacket) for subpacket in packets_hierarchy["subpackets"])
    elif packets_hierarchy["id"] == 4:
        return packets_hierarchy["literal_value"]
    elif packets_hierarchy["id"] == 5:
        first_subpacket = decode_value(packets_hierarchy["subpackets"][0])
        second_subpacket = decode_value(packets_hierarchy["subpackets"][1])
        if first_subpacket > second_subpacket:
            return 1
        else:
            return 0
    elif packets_hierarchy["id"] == 6:
        first_subpacket = decode_value(packets_hierarchy["subpackets"][0])
        second_subpacket = decode_value(packets_hierarchy["subpackets"][1])
        if first_subpacket < second_subpacket:
            return 1
        else:
            return 0
    elif packets_hierarchy["id"] == 7:
        first_subpacket = decode_value(packets_hierarchy["subpackets"][0])
        second_subpacket = decode_value(packets_hierarchy["subpackets"][1])
        if first_subpacket == second_subpacket:
            return 1
        else:
            return 0
    else:
        print("Error")

if __name__ == '__main__':

    bits_sequence = hex_to_bit_sequnece(get_input_of_day(16))
    packets_hierarchy,bits_seq = parse_packets(bits_sequence)
    print("Day 16 part 1 answer: {}".format(sum_versions(packets_hierarchy)))
    print("Day 16 part 2 answer: {}".format(decode_value(packets_hierarchy)))
