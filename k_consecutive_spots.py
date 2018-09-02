"""
Find when K consecutive spots are empty
given an array which determines the position
in which an element is inserted
arr : [2, 3, 4, 1, 5]
arr1: [2, 3, 5, 1, 4]

subtract 1, to get 0 indexed
[1, 2, 3, 0, 4]

[_,_,_,_,_] 1
[_,1,_,_,_] 2
[_,1,1,_,_] 3    ---> STOP, as two consecutive empty spots found
[_,1,1,1,_]
[_,_,_,_,_]
[_,_,_,_,_]
[_,_,_,_,_]

Soln:
keep P list of indices :
[0,5]  -> 2
[0,1], [2,5] -> 3
[0,1], [3,5] -> 5 == 2
[0,1], [3,4]
for each insertion, you are iterating over ^ (but this list is sorted)
for each insertion, check the lower bound? or upper bound? (check both) - but binary search through the array

dict: keeps track of the distance to closest full space from P given full position
{
  0: (1, f)
  1: (1, t)
  2: (4, t)
  3: (4, f)
  4: (4, f)
}


[2, 3, 4, 1, 5]
#[1 ,2, 3, 0, 4]


------------------------------------------------------------------

TreeMap - map[len(map)/2]
[1,_,2,5,_]

{
   lb  ub of contiguous free space
    0: 1
    2: 2
    3: 5
}

set current upper bound to index
create new key -> index+1, set upper bound of this key to be previous key's upper bound


---------------------------------
=
# we can potentially convert this dictionary into an array and then think about the sorting issue/ logn search

Take care of off by 1 errors
"""
# def k_spots_empty(P, K, index, closest_full_spot):
#     # reached the end
#     if index == len(P):
#         return -1
#
#     for pos in closest_full_spot:
#         if closest_full_spot[pos] - pos == K:
#             print pos, closest_full_spot
#             return index
#     # insert element at index - update closest_full_spot
#     for pos in closest_full_spot:
#         if pos <= index and closest_full_spot[pos] > index:
#             closest_full_spot[pos] = index
#
#     # recurse with index+1
#     return k_spots_empty(P, K, index+1, closest_full)
#
# def find_k_empty_spots(P,K):
#     closest_full_spot = {}
#     for i in range(len(P)):
#         closest_full_spot[i] = len(P)-1
#     return k_spots_empty(P,K,0, closest_full_spot)


#arr = [2, 3, 4, 1, 5]
#arr = [1, 2, 3, 0, 4]
arr = [2,5,1,4,3]

#print find_k_empty_spots(arr, 2)
# [f,f,f,f,f]
def find_k_empty_dumb(P,K):
    for i in range(len(P)):
        P[i] = P[i]-1
    empty = [True for i in range(len(P))]
    for i, num in enumerate(P):
        empty[num] = False
        count = 0
        for spot in empty:
            if spot == False:
                if count == K:
                    return i+1
                count = 0
            else:
                count+=1
        if count == K:
            return (i, num)
    return -1
print find_k_empty_dumb(arr, 2)
