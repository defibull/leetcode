def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        h = {}
        adding = True
        count = 1
        for i in range(len(s)):
            if count in h:
                h[count].append(s[i])
            else:
                h[count] = [s[i]]

            if count == numRows:
                adding = False
            if count == 1:
                adding = True
            if adding:
                count+=1
            else:
                count-=1
        return "".join([ch for sublist in h.values() for ch in sublist])
