def permutations(s, curr, res=[]):
    if not s:
        res.append(curr)
        return res
    for i, char in enumerate(s):
        permutations(s[:i]+s[i+1:], curr+char, res)
    return res

print(permutations("cat",""))
