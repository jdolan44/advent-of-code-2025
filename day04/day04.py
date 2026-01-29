file = open("day04.txt", "r")
floor = file.read().split("\n")

def in_range(i, j):
    return i>=0 and j>=0 and i<len(floor) and j<len(floor[i])

def is_forkliftable(i, j):
    if(floor[i][j] != '@'): return False
    
    total = 0
    for x in range(-1, 2):
        for y in range(-1, 2):
            if in_range(i+x, j+y) and floor[i+x][j+y] == '@': total+=1
    return total <=4

#part 1
# total = 0
# for i in range(0, len(floor)):
#     for j in range(0, len(floor[i])):
#         if is_forkliftable(i, j): total+=1

total = 0
removed = True
while removed:
    removed = False
    for i in range(0, len(floor)):
        for j in range(0, len(floor[i])):
            if is_forkliftable(i, j): 
                total+=1
                floor[i] = floor[i][:j] + 'x' + floor[i][j + 1:]
                removed = True

print(total)
