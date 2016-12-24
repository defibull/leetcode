def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        curr_len = 0
        max_len = 0
        p = [[False for j in range(n)] for i in range(n)]
        palindrome_starts_at = 0
        # len = 1
        for i in range(n):
            p[i][i] = True
            max_len = 1
        # len = 2
        for i in range(n-1):
            if s[i] == s[i+1]:
                p[i][i+1] = True
                max_len = 2
                palindrome_starts_at = i
        # len > 2
        for length in range(3,n+1):
            for i in range(n-length+1):
                j = i+length-1
                if s[i] == s[j] and p[i+1][j-1]:
                    p[i][j] = 1
                    if max_len < length:
                        palindrome_starts_at = i
                        max_len = length

        return s[palindrome_starts_at:palindrome_starts_at+max_len]
