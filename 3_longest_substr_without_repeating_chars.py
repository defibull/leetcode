def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = 0
        count = 0
        seen = set()
        i = 0
        j = 0
        n = len(s)
        while i < n and j < n:
            if s[j] not in seen:
                seen.add(s[j])
                j+=1
            else:
                if s[i] in seen:
                    seen.remove(s[i])
                i+=1
            m = max(m,len(seen))
        return m
