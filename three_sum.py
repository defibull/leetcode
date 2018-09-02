"""
Problem with this solution: This would run but its too slow

"""
def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    all_results = set()
    for j, num in enumerate(nums):
        res = twoSum(-1*num, nums[:j]+nums[j+1:])
        for each_result in res:
            if len(each_result) == 2:
                each_result.append(num)
                each_result.sort()
                all_results.add(tuple(each_result))
    return list(all_results)

def twoSum(target, numList):
    h = {}
    results = []
    for i, num in enumerate(numList):
        if target-num in h:
            results.append([target-num, num])
        else:
            h[num] = i
    return results

print(threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))
