import pprint
def longestPalindrome(A):
        n = len(A)
        dp = [[False for j in range(n)] for i in range(n)]
        max_i = 0
        max_len = 0
        for i in range(n):
            dp[i][i] = True
            max_len = 1

        #len = 2
        seen = False
        for i in range(n-1):
            if A[i] == A[i+1]:
                dp[i][i+1] = True
                if not seen:
                    max_i = i
                    seen = True
                max_len = 2

        #len > 2
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(dp)
        for curr_len in range(3,n+1):
            for i in range(0,n-curr_len+1):
                j = i+curr_len-1
                print i,j
                if A[i] == A[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    if curr_len > max_len:
                        max_i = i
                        max_len = curr_len


        # print max_i, max_len
        return A[max_i: max_i+max_len+1]
print longestPalindrome('aaaabaaa')
