from heapq import *
def solve(A, B):
    n = len(A)
    if n < 1:
        return []
    A.sort()
    B.sort()
    ans = []
    heap = []
    heappush(heap, (-1*(A[n-1]+B[n-1]), n-1, n-1))
    k = n
    s = set()
    while k:
        print heap
        a = heappop(heap)
        ans.append(-1*a[0])
        L = a[1]
        R = a[2]
        if R >= 0 and L > 0 and (L-1, R) not in s:
            s.add((L-1,R))
            heappush(heap, (-1*(A[L-1]+B[R]), L-1, R))
        if R > 0 and L >=0 and (L,R-1) not in s:
            s.add((L,R-1))
            heappush(heap, (-1*(A[L]+B[R-1]), L, R-1))
        k-=1
    return ans

ai = [3,2,4,2]
bi = [4,3,1,2]

print solve(ai,bi)
