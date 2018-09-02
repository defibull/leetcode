
def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    results = []
    nums.sort()
    i = 0
    while i < len(nums):
        target = -nums[i]
        j, k = 0,len(nums)-1
        while j < k:
            # print i,j,k
            if i != j and j != k:
                if nums[j] + nums[k] == target:
                    results.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j+=1
                    while j < k and nums[k] == nums[k-1]:
                        k-=1
                    j+=1
                    k-=1
                elif nums[j] + nums[k] > target:
                    k-=1
                else:
                    j+=1
            if i==j:
                j+=1

        i+=1
    return results
print threeSum([-1,0,1,2,-1,-4])
