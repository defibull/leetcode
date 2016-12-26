    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        negative = False
        ans = 0
        if x < 0:
            negative = True
        x = abs(x)
        while x != 0:
            supplement = x%10
            x = x/10
            ans = ans*10 + supplement

        if ans >= 2147483647:
            return 0

        if negative:
            return -1*ans

        return ans
