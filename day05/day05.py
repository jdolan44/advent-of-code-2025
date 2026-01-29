file = open("day05.txt", "r")
ranges = []
ids = []

for line in file:
    if "-" in line:
        first_num = int(line[:line.index("-")])
        last_num = int(line[line.index("-")+1:].strip())
        ranges.append((first_num, last_num))
    elif line.strip():
        ids.append(int(line.strip()))

def is_fresh(id):
    for (start, end) in ranges:
        if id >= start and id <= end: return True
    return False

#part 1
def total_fresh_from_list():
    total = 0
    for id in ids:
        if(is_fresh(id)): total +=1
    return total

#part 2
def overlap(range1, range2):
    #not... range 1 begins after range 2 ends OR range 2 begins after range 1 ends.
    return not (range1[0] > range2[1] or range2[0] > range1[1])

def combine_ranges(range1, range2):
    lowest = min(range1 + range2)
    highest = max(range1 + range2)
    return (lowest, highest)


def total_fresh():
    pass
    # total = 0
    # counts = [True for r in ranges]
    # for i in range(0, len(ranges)):
    #     for j in range(0, len(ranges)):
    #         if counts[i] and counts[j] and overlap(ranges[i], ranges[j]) and i != j:
    #             ranges[i] = combine_ranges(ranges[i], ranges[j])
    #             counts[j] = False
    
    # print(ranges)
    # print(counts)
    # for i in range(0, len(ranges)):
    #     if counts[i]: total += ranges[i][1] - ranges[i][0] + 1
    # return total



print("total fresh from list:", total_fresh_from_list())
print("part 2:", total_fresh())

