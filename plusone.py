def plusOne(A):
        result = []
        carry = 0
        count = 0
        for num in reversed(A):
            if count == 0:
                result.append((num+1+carry)%10)
                count = 1
            else:
                result.append((num+carry)%10)
            carry = (num+1+carry)/10
            print carry
        if carry:
            result.append(1)
        return result[::-1]
print plusOne([ 1, 1, 1, 3, 2, 1, 1, 2, 5, 9, 6, 5])
