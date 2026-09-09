class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0 #pointers
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        if i == len(s): #only reaches len of s if true
            return True
        else:
            return False