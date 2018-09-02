# class Node(object):
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None
#
#
# def inorder(root):
#     if root:
#         left = inorder(root.left)
#         val = root.val
#         right = inorder(root.right)
#         return [left, val, right]
#
#
#
# root1 = Node(2)
# root1.left = Node(1)
# root1.left.left = Node(0)
# root1.right = Node(3)
# print inorder(root1)

l = [[1,2,3], 4, 5]

def inorder(listOflists):
    results = []
    for elem in listOflists:
        if isinstance(elem, (int, long, float, complex)):
            results.append(elem)
        else:
            results.extend(elem)
    return results

def inorder_rec(listOflists, results=[]):
    if len(listOflists) == 0:
        return results
    if isinstance(listOflists[0], (int, long, float, complex)):
        results.append(listOflists[0])
    else:
        results.extend(listOflists[0])
    return inorder_rec(listOflists[1:], results)


def inorder_rec2(listOflists, results=[]):
    if len(listOflists) == 0:
        return results
    if isinstance(listOflists[0], (int, long, float, complex)):
        results.append(listOflists[0])
    else:
        inorder_rec(listOflists[0], results)
    return inorder_rec(listOflists[1:], results)

# print inorder(l)
print inorder_rec(l)
print inorder_rec2(l)
    # if
    # if isinstance(listOflists[0], (int, long, float, complex)):
    #     results.append(listOflists[0])
    # else:
    #
