def search_f(A, B, sf):
        low = 0
        count = 0
        high = len(A)-1
        res = -1
        while low < high:
            mid = (low+high)/2
            if A[mid] == B:
                print mid,low, high
                res = mid
                if sf:
                    high = mid-1
                else:
                    low = mid+1
            elif A[mid] > B:
                high = mid-1
            else:
                low = mid+1
        return res
def findCount(A, B):
        start = search_f(A, B, True)
        if start == -1:
            return 0
        end = search_f(A, B, False)
        return (end - start) + 1
print findCount([ 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 7, 7, 8, 8, 8, 8, 9, 9, 10, 10, 10 ], 1)
