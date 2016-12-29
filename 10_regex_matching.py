def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s == None or p == None:
            return False

        dp = [[False for j in range(len(p)+1)] for i in range(len(s)+1)]
        dp[0][0] = True

        for j in range(1,len(dp[0])):
            if p[j-1] == "*":
                if dp[0][j-1] or (j > 1 and dp[0][j-2]):
                    dp[0][j] = True

        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1] == s[i-1] or p[j-1] == ".":
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*":
                    if s[i-1] != p[j-2] and p[j-2] !=".":
                        dp[i][j] = dp[i][j-2]
                    else:
                        dp[i][j] = dp[i-1][j] or dp[i][j-1] or dp[i][j-2]

        return dp[len(s)][len(p)]
