def findMaxLength( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    return find_biggest(nums)

def find_biggest( remaining):
    count0,count1 = 0,0
    for num in remaining:
        if num == 0:
            count0+=1
        elif num == 1:
            count1+=1
    if count0 == count1:
        return len(remaining)
    else:
        if count0 > count1:
            #remove the 0 closest to one of the ends
            removed = False
            start,end = 0, len(remaining)
            while not removed:
                if remaining[start] == 0:
                    start+=1
                    removed = True
                elif remaining[end-1] == 0:
                    end-=1
                    removed = True
                else:
                    start+=1
                    end-=1
            return find_biggest(remaining[start:end])
        elif count1> count0:
            #remove closest 1 to the ends
            removed = False
            start,end = 0, len(remaining)
            while not removed:
                if remaining[start] == 1:
                    start+=1
                    removed = True
                elif remaining[end-1] == 1:
                    end-=1
                    removed = True
                else:
                    start+=1
                    end-=1
            return find_biggest(remaining[start:end])
print findMaxLength([0,1,1])
