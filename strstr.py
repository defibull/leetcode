# def strStr(haystack, needle):
#         if len(haystack) == 0 or len(needle) == 0:
#             return -1
#         i = 0
#         j = 0
#         found = False
#         first = -1
#         while i < len(haystack) and j < len(needle):
#             print i, j, first
#             if haystack[i] == needle[j]:
#                 if not found:
#                     first = i
#                     found = True
#                 i+=1
#                 j+=1
#             else:
#                 if found:
#                     j = 0
#                     first = -1
#                     found = False
#                 else:
#                     i+=1
#                     j = 0
#                     first = -1
#         if j == len(needle):
#             return first
#         else:
#             return -1

def strStr (haystack, needle):
        if len(haystack) == 0 or len(needle) == 0:
            return -1
        for i, c in enumerate(haystack):
                for j, n in enumerate(needle):
                    if j == 0:
                        found = True
                    if i+j < len(haystack) and haystack[i+j] != n:
                        found = False
                    if j == len(needle)-1 and i+j < len(haystack) and haystack[i+j] == n and found:
                        print i, j, haystack[i+j], n, found
                        return i
        return -1
# print strStr("bbbbbbbbab", "baba")
# print strStr("bbaabbbbbaabbaabbbbbbabbbabaabbbabbabbbbababbbabbabaaababbbaabaaaba", "babaaa")
print strStr("bbbabbabbbaabababaaaaaababaaabbabbabbabbaaaabbbbbbaabbabbbbbabababbaaabbaabbbababbb", "bba")
