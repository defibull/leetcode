def setZeroes(A):
        zero_first_row = False
        zero_first_col = False
        for j in range(len(A[0])):
            if A[0][j] == 0:
                zero_first_row = True
        for i in range(len(A)):
            print A
            if A[i][0] == 0:
                zero_first_col = True
                print "true"
        for i in range(1,len(A)):
            for j in range(1,len(A[0])):
                if A[i][j] == 0:
                    A[0][j] = 0
                    A[i][0] = 0

        for i in range(1,len(A)):
            for j in range(1,len(A[0])):
                if A[0][j] == 1 and A[i][0] == 1:
                    A[i][j] = 1
                else:
                    A[i][j] = 0
        if zero_first_row:
            A[0] = [0 for i in range(len(A[0]))]
        if zero_first_col:
            for i in range(len(A)):
                A[i][0] = 0
                print "made"
        return A
print setZeroes([[0,1],[1,1]])
