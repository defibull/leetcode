with open('rosalind4.txt', 'rw') as f:
    read = f.read().split(" ")
sum = 0
for i in range(int(read[0]), int(read[1])+1):
    if i % 2 == 1:
        sum+=i
print sum
