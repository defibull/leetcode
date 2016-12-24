def getMedian(self,nums):
        n = len(nums)
        if n == 0:
            return 0
        elif n%2 ==0:
            return float(nums[n/2] + nums[(n/2)-1])/2
        else:
            return nums[n/2]

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        pass
