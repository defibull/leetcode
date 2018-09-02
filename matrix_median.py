def count_small_or_eq(B,x):
        low = 0
        high = len(B)-1
        curr = -1
        while low <= high:
            mid = (low+high)/2
            if B[mid] <= x:
                curr = mid
                low = mid+1
            else:
                high = mid-1
        return curr +1

def findMedian( A):
        for row in A:
            for i, num in enumerate(row):
                s = i
                for nc_row in A:
                    print s
                    if nc_row == row:
                        continue
                    s+=count_small_or_eq(nc_row,num)
                if s == int(len(A)*len(A[0]))/2:
                    return num
print findMedian([
  [2],
  [1],
  [4],
  [1],
  [2],
  [2],
  [5]
])
