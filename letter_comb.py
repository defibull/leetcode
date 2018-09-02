def letter_combinations(A):
    return letterCombinations(A, "", [])

def letterCombinations(A,s, result):
    if len(A) == 0:
        result.append(s)
        s = ""
        return
    for ch in d[A[0]]:
        letterCombinations(A[1:],s+ch, result)
    return result

d = {"2":"abc", "3":"def","4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz" }
print letter_combinations("2")
print letter_combinations("4")

#LESSON: if you
