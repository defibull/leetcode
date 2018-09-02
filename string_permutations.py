def perm(s):
    return permutations(s,"",[])
def permutations(s,start, res):
    if not s:
        res.append(start)
        return
    for ch in s:
        permutations("".join([i for i in s if i!=ch]), start+ch, res)
    return res

print perm("cat")
