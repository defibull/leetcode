#key concept : hash(word1)+hash(word2) = hash(word2)+hash(word1)
def findSubstring(A, B):
    # A == S, B == L
    ans = []
    lsize = len(B)
    if not B:
        return []
    wsize = len(B[0])
    hashsum = 0
    for word in B:
        hashsum+=hash(word)
    for i in range(0, len(A)- (wsize*lsize-1)):
        h = 0
        for j in range(lsize):
            h+=hash(A[i+j*wsize:(i+j*wsize)+wsize])
        if h == hashsum:
            ans.append(i)

    return ans

print findSubstring("barfoothefoobarman", ["foo", "bar"])
