def isPalindrome(A):
    return list(A) == list(reversed(A))

def partition(A):
    return part(A,0, [], [])
def part(A,i,cur,res):
    if i == len(A):
        res.append(cur)
        return
    for j in range(i, len(A)):
        sub = A[i:j+1]
        if isPalindrome(sub):
            part(A,j+1, cur +[sub], res)
    return res




s = "aaab"
print partition(s)
