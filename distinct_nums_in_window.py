def dNums(A, B):
        k = B
        h = {}
        ans = []
        for i in range(0, len(A)-(k-1)):
            print h
            if i == 0:
                for j in range(i, i+k):
                    if A[j] in h:
                       h[A[j]]+=1
                    else:
                        h[A[j]] = 1
                ans.append(len(h))
            else:
                #remove and added
                h[A[i-1]]-=1
                if h[A[i-1]] == 0:
                    del h[A[i-1]]
                if A[i+k-1] in h:
                    h[A[i+k-1]]+=1
                else:
                    h[A[i+k-1]] = 1
                ans.append(len(h))
        print h
        return ans

A_test = [ 1, 2, 1, 3, 4, 3 ]
B_test = 3

print dNums(A_test, B_test)
