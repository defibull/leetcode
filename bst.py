class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class BST:
#     def __init__(self):
#         self.root = None
#     def insert(self, value):
#         return self.insertBST(self.root, value)
def insertBST(root,value):
    if root == None:
        root = Node(value)
        return root
    else:
        if value < root.val:
            root.left = insertBST(root.left, value)
        elif value > root.val:
            root.right = insertBST(root.right, value)
    return root

def printBST(root):
    if root == None:
        print "root is None"
        return
    print root.val
    if root.left:
        print "/"
        printBST(root.left)
    if root.right:
        print "\\"
        printBST(root.right)

def isValidBST(A):
        if A == None:
            return 1
        return isSubTreeless(A.left, A.val) and isSubtreeGreater(A.right, A.val) and isValidBST(A.left) and isValidBST(A.right)

def isSubTreeless(root,val):
    if root == None:
        return 1
    if root.val <= val:
        print "root.val=", root.val, "val=", val
        return isSubTreeless(root.left, val) and isSubTreeless(root.right,val)
    else:
        print "root.val=", root.val, "val=", val
        return 0
def isSubtreeGreater(root,val):
    if root==None:
        return 1
    if root.val > val:
        print "root.val=", root.val, "val=", val
        return isSubtreeGreater(root.left, val) and isSubtreeGreater(root.right,val)
    return 0


root1 = Node(1)
insertBST(root1,2)

insertBST(root1,0)
insertBST(root1,3)
insertBST(root1, 1.5)
# for i in range(3,6):
#     insertBST(root1, i)
# printBST(root1)
print isValidBST(root1)
