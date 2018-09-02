def subsets(A):
    A.sort()
    l =  subset_list(A, [], [])
    l.insert(0,[])
    return l
def subset_list(A, start, res):
    if len(A) < 1:
        return
    for i , num in enumerate(A):
        print start, i, A[i]
        res.append(start+[A[i]])
        subset_list(A[i+1:], start+[A[i]], res)
    return res

S = [1,2,3]
s = [ 15, 20, 12, 19, 4 ]
print subsets(s)
