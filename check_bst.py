# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.data = x
#         self.left = None
#         self.right = None
def isValidBST(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if not root:
        return True
    return ((not root.right or 
        (root.right.data > root.val and validateBigger(root.right, root.val) and isValidBST(root.right))) and 
        (not root.left or 
         (root.left.data < root.val and self.validateSmaller(root.left, root.val) and isValidBST(root.left))))
def validateSmaller(root, val):
    if not root:
        return True
    return root.data < val and validateSmaller(root.left, val) and validateSmaller(root.right, val)
def validateBigger(root, val):
    if not root:
        return True
    return root.data > val and validateBigger(root.left, val) and validateBigger(root.right, val)
