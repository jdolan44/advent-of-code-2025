file = open("day03.txt", "r")
lines = file.read().split("\n")

def get_highest_index(string, start, end):
    highest_index = start
    for i in range(start, end):
        if int(string[i]) > int(string[highest_index]): 
            highest_index = i
    return highest_index

def get_joltage(string, num_digits = 2):
    joltage = ""
    highest_index = -1
    for i in range(num_digits-1, -1, -1):
        highest_index = get_highest_index(string, highest_index+1, len(string)-i)
        joltage += string[highest_index]
    return int(joltage)

total = 0
for line in lines:
    total += get_joltage(line, 12)

print(total)