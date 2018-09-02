from collections import deque
import operator
class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        q = deque(A)
        nums = []
        ops = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.div }
        while q:
            print q, nums
            if q[-1].isdigit():
                break
            obj = q.popleft()
            if obj not in ops:
                nums.append(int(obj))
            elif obj in ops:
                op = obj
                num1 = nums.pop()
                num2 = nums.pop()
                ans = ops[op](num2,num1)
                print ans
                q.appendleft(str(ans))

        return q.pop()
sol = Solution()
# A = ["2", "2", "/"]
A = [ "5", "1", "2", "+", "4", "*", "+", "3", "-" ]
print sol.evalRPN(A)
