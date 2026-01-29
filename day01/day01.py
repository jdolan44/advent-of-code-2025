file = open("day01.txt", "r")
turns = file.read().split("\n")

def turn_left(num, dial, counter):
    for i in range(0, num):
        dial -= 1
        if dial == 0: counter +=1
        if dial == -1: dial = 99 #dial % 100
    return (dial, counter)

def turn_right(num, dial, counter):
    for i in range(0, num):
        dial += 1
        if dial == 100: 
            dial = 0 #dial % 100
            counter +=1
    return (dial, counter)

dial = 50
counter = 0

for turn in turns:
    num = int(turn[1:])
    if turn[0] == 'L':
        dial, counter = turn_left(num, dial, counter)
    else:
        dial, counter = turn_right(num, dial, counter)
print(counter)