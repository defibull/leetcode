 def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        s = str.strip()
        if not s:
            return 0
        ans = 0
        sign = 1
        if s[0] == "-":
            sign = -1*sign
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]
        while s:
            curr = s[0]
            s = s[1:]
            if curr.isdigit():
                ans = ans*10 + (ord(curr) - ord('0'))
            if ans == 0 and not curr.isdigit():
                return 0
            if ans !=0 and not curr.isdigit():
                break
        ans = sign*ans
        if ans >= 2147483647:
            ans = 2147483647
        elif ans <= -2147483648:
            ans = -2147483648
        return ans
