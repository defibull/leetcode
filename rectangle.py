G = 6
#print [(l, w) for l in range(A+1) for w in range(l+1) if l*(w) == A]

# 1 6
# 2 3
# 3 2
# 6 1


def coni(area):
    minimize = [(l, w) for l in range(area+1) for w in range(l+1) if l*(w) == area]
    return min(minimize, key=lambda x: x[0]-x[1])

def minimize(area):
    return min(((l, w) for l in range(area+1) for w in range(l+1) if l*(w) == area), key=lambda x: x[0]-x[1] )
print minimize(G)
