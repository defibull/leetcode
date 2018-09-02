import fileinput
mat = []
for line in fileinput.input():
        mat.append(line)

def isvalid(mat):
    queens = []
    for row in mat:
        queens.append(row.index("*"))

    return (len(set(queens)) == len(queens)) and check_diagonals(queens)
def check_diagonals(rows):
    for r1, c1 in enumerate(rows):
        for r2,c2 in enumerate(rows):
            if r1 != r2:
                if abs(r1-r2) == abs(c1-c2):
                    return False
    return True
print "valid" if isvalid(mat) else "invalid"
