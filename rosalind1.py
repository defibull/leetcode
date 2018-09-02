with open('rosalind_ini3.txt', 'rw') as f:
    read_data = f.read()
read = read_data.split("\n")
li = read[1].split(" ")
i1 , i2, i3,i4 = int(li[0]), int(li[1]), int(li[2]), int(li[3])
s = read[0]
print s[i1:i2+1], s[i3:i4+1]
