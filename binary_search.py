def binary_search(A,target):
    if len(A) == 0:
        return False
    mid = len(A)/2
    if A[mid] == target:
        return True
    elif A[mid] < target:
        return binary_search(A[mid+1:],target)
    else:
        return binary_search(A[:mid],target)

A = [1,2,3,4,5]
print binary_search(A, 5)
