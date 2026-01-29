file = open("day02.txt", "r")
ranges = file.read().split(",")

total = 0
#int -> boolean
def is_invalid(i):
    istring = str(i)
    for i in range(1, len(istring)):
        compareString = istring[:i] * (len(istring) // i)
        if compareString == istring: 
            #print(istring)
            return True
    return False

for r in ranges:
    left, right = map(int, r.split("-"))
    for i in range(left, right+1):
        if(is_invalid(i)): total+=i

print(total)
