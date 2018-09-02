def two_sum_0(A):
    n = len(A)
    i,j = 0,n-1
    while i < n and j > 0:
        if A[i] + A[j] > 0:
            j-=1
        elif A[i]+A[j] < 0:
            i+=1
        else:
            return [i,j]
    return [-1,-1]
A = [-1,1,2,3,4]
print two_sum_0(A)
