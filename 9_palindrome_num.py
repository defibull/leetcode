"""
Python has no integer overflow
"""
def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        n = x
        rev = 0
        while n :
            rev = rev*10 + n%10
            n /=10
        if rev == x:
            return True
        else:
            return False
