import fileinput
def proper_fraction(num, denom):
    num = int(num)
    denom = int(denom)
    quo = num/denom
    print quo, num - quo*denom, "/", denom

for line in fileinput.input():
    num, denom = line.strip().split(" ")
    if num == "0" and denom == "0":
        break
    proper_fraction(num, denom)
