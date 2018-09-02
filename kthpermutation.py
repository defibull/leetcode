def getPermutation(A):
    return permute(A,[],[],3)
def permute(A,start,res,limit):
    if len(A) < 1:
        res.append(start)
        return
    for num in A:
        print num,A
        permute([i for i in A if i!=num], start +[num], res,limit)
        if len(res) == limit:
            return res

    return res
print getPermutation([1,2,3])

def iterative_perm(A):
    fact = []
    sum  = 1
    fact[0] = 1
    for i in range(1,n+1):
        sum*=i
        fact.append(sum)
    n_list = [i for i in range(1,n+1)]
    k-=1
    res = []
    for i in range(1,n+1):
        index = k/fact[n-i]
        res.append(str(n_list[index]))
        n_list.pop(index)
        k-=fact[n-i]*index
    return "".join(res)
