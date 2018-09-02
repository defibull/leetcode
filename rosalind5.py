from collections import Counter
with open('rosalind_dna.txt', 'rw') as f:
    read = f.read()
c = Counter(read)
print c
print c['A'], c['C'], c['G'], c['T']
