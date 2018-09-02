def countPairs(k,a):
    h = {}
    count = 0
    for num in a:
        if k - num in h:
            count+=h[k-num]
        if num in h:
            h[num]+=1
        elif num not in h:
            h[num] = 1
    return count

print countPairs(2,[1,2,3,1])

# 1a + 1b
# 1a + 1c
# 1a + 1d
# 1b + 1c
# 1b + 1d
# 1c + 1d
