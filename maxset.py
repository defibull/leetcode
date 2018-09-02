def maxset(A):
        n = len(A)
        m = [0,0,0]
        curr = 0
        i , j = 0 , 0
        if len(A) < 2:
            return A
        while i < n and j < n:
            print curr,i,j
            if A[j] >= 0:
                curr+=A[j]
                print "curr after add", curr
                j+=1
            else:
                if m[0] < curr:
                    m = [curr, i , j]
                elif m[0] == curr and (j-i) > (m[2] - m[1]):
                    m = [curr, i, j]
                j+=1
                i=j
                curr = 0
        if m[0] < curr:
            m = [curr, i , j]
        elif m[0] == curr and (j-i) > (m[2] - m[1]):
            m = [curr, i, j]
        return A[m[1]: m[2]]
print maxset([0,0,-1,0])
print maxset([ 756898537, -1973594324, -2038664370, -184803526, 1424268980 ])
b = [ 756898537, -1973594324, -2038664370, -184803526, 1424268980 ]
print b[3:4]
