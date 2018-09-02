from collections import Counter
with open('rosalind_ini6.txt', 'rw') as f:
    read_text = f.read()
read = read_text.split(' ')
read = [i.strip('\n') for i in read]
c = Counter(read)
for key in c:
    print key, c[key]
