from __future__ import print_function
with open('rosalind_ini5.txt', 'rw') as f:
    for i, line in enumerate(f):
        if i%2 == 1:
            print(line, end="")
