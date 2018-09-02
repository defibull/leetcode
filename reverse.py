def reverse_n_squared(a):
    rev_a = list(reversed(a))
    ans = []
    start = 0
    for i, char in enumerate(rev_a):
        if char == ' ':
            ans.extend(list(reversed(rev_a[start:i])))
            ans.extend(' ')
            start = i
            start+=1

    ans.extend(list(reversed(rev_a[start:])))
    return ans

def reverse_n(a):
    rev_a = (("".join(a)).split(" "))[::-1]
    return list(" ".join(rev_a))


arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', ' ', 'm', 'a', 'k', 'e', 's', ' ', 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]
# print reverse_n_squared(arr)
print reverse_n(arr)
