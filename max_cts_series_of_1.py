# def maxone(A, B):
#         max_len = 0
#         start,finish = 0,0
#         i,j = 0,0
#         n = len(A)
#         print n, A[36]
#         flips = B
#         while i < n and j <= n:
#             if (j == n or A[j] == 0) and flips <= 0:
#                 if j-i > max_len:
#                     max_len = (j-i)+1
#                     start , finish = i,j
#                 if j == n:
#                     break
#                 #start with next one
#                 i+=1
#                 print i
#                 while i < n and A[i] != 1:
#                     i+=1
#                 j = i
#                 # j+=1
#                 # i = j
#                 flips = B
#             if j == n:
#                 break
#             elif j < n and A[j] == 1:
#                 j+=1
#             elif j < n and A[j] == 0 and flips:
#                 flips-=1
#                 j+=1
#
#         return [i for i in range(start,finish)]
def maxone(A, B):
        i,j,n = 0,0, len(A)
        count = 0
        m = 0
        st = 0
        while i < n and j < n:
            print i,j
            if A[j] == 1:
                j+=1
            elif A[j] == 0:
                if count < B:
                    j+=1
                else:
                    if m < j-i:
                        m = j-i
                        st = i
                    while not (count < B):
                        if A[i] == 0 and B > 0:
                            count -=1
                        print i
                        i+=1
                        if j < i:
                            j=i
                    j+=1
        if m < j-i:
            m = j-i
            m+=1 #j not at 0 now
            st = i
        return [i for i in range(st,m)]
        # return A[st:m]

# A = [0,1,1,1]
# B = 0
A = [ 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0 ]
B = 0
print maxone(A,B)
