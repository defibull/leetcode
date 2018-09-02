def countArrangement(N):
    """
    :type N: int
    :rtype: int
    """
    return count_arrangements(0,[],N)

def count_arrangements(index,start,N):
    if len(start) == N:
        addCount = True
        for i in range(len(start)):
            if start[i]%(i+1)!=0 and (i+1)%start[i] !=0:
                return 0
        return 1
    count = 0
    for num in range(1,N+1):
        if num not in start and (num%(index+1)== 0 or (index+1)%num == 0):
            add_to_count = count_arrangements(index+1,start+[num],N)
            count+=add_to_count
    return count

print countArrangement(10)
