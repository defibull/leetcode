class Position(object):
    def __init__(self,r,c):
            self.r = r
            self.c = c
def solveNQueens(A):
    null_pos = Position(-1,-1)
    positions = [null_pos for i in range(A)]
    solutions = getSolns(A, 0, positions, [])
    return solutions

def getSolns(n,row,pos, res):
    if row == n:
        oneresult = []
        buff = []
        for position in pos:
            for i in range(n):
                if position.c == i:
                    buff.append("Q")
                else:
                    buff.append(".")
            oneresult.append("".join(buff))
            buff = []
        res.append(oneresult)
    for col in range(n):
        found_place = True
        for queen in range(row):
            if pos[queen].c == col or (pos[queen].r - pos[queen].c) == row-col or (pos[queen].r + pos[queen].c) == row+col:
                found_place = False

        if found_place:
            pos[row] = Position(row, col)
            getSolns(n,row+1,pos,res)

    return res

print solveNQueens(1)
