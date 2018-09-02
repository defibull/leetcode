import re
m = []
with open('rosalind_cons.txt', 'rw') as f:
    read_data = f.read()
    # for i, line in enumerate(f):
    #     print len(line)
    #     if i%2 == 1:
    #         m.append(list(line.strip('\n')))
read = re.split('>Rosalind_[0-9]+', read_data) #read_data.split('')
for i , line in enumerate(read):
    if len(line) == 0:
        continue
    m.append(list(line.replace("\n","")))

p = [[0 for j in range(len(m[0]))] for i in range(4)]


for c in range(len(m[0])):
    col = [m[row][c] for row in range(0,len(m))]
    print col
    p[0][c] = col.count('A')
    p[1][c] = col.count('C')
    p[2][c] = col.count('G')
    p[3][c] = col.count('T')
s = []
index = ['A','C', 'G', 'T']
for c in range(len(m[0])):
    max_row = 0
    max_num = 0
    for row in range(0,4):
        if p[row][c] > max_num:
            max_row = row
            max_num = p[row][c]
    s.append(index[max_row])

print "".join(s)

print "A:", " ".join(str(x) for x in p[0])
print "C:", " ".join(str(x) for x in p[1])
print "G:", " ".join(str(x) for x in p[2])
print "T:", " ".join(str(x) for x in p[3])
