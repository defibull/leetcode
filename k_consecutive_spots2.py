"""
n flower pots, every flower pot flowers, array determines which day is which. You have  to return the first day that results in K continous empty flower pot chain

"""

##
# This soln is not
##


def find_consecutive(P,K):
    for i in range(len(P)):
        P[i] = P[i]-1
    #  {lb(ub index) : upper bound of contiguous free space}
    ub = {0:len(P)}
    for i, num in enumerate(P):
        lb_key = binary_search(ub.keys(), num, ub)
        original_ub = ub[lb_key]
        ub[lb_key] = num
        ub[num+1] = original_ub
        if (num - lb_key == K) or (original_ub - (num+1) == K):
            return i+1
    return -1
    def binary_search(keys, target, h):
        mid = len(keys)/2
        print keys, target, mid
        if keys[mid] == target or (keys[mid] < target and h[keys[mid]] > target):
            return keys[mid]
        if keys[mid] < target:
            return binary_search(keys[mid+1:], target, h)
        else:
            return binary_search(keys[:mid], target, h)
# print "[1, 2, 3, 0, 4]"
# print find_consecutive([1, 2, 3, 0, 4], 2)
# print (find_consecutive ([2,5,1,4,3], 2))
print (find_consecutive([2, 4, 3, 1, 5], 2))
## need self balancing binary search tree?
#
# class Node(object):
#     def __init__(self, lb, ub):
#         self.lb = lb
#         self.ub = ub
#         self.left = None
#         self.right = None
#     def insert(self, val):
