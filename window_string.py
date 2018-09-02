from collections import Counter
import sys
def minWindow(S, T):
    m = Counter(T)
    counter = len(T)
    begin,end,minStart,minLen= 0,0,0,sys.maxsize
    while end < len(S):
        if S[end] in m:
            if m[S[end]]>0:
                counter-=1
            m[S[end]]-=1

        while counter == 0:
            if end-begin+1 < minLen:
                minLen = end-begin+1
                minStart = begin
            if S[begin] in m:
                m[S[begin]]+=1
                if m[S[begin]] > 0:
                    counter+=1
            begin+=1
        end+=1

    return S[minStart:minStart+minLen]



print minWindow("ADOBECODEBANC", "ABC")
