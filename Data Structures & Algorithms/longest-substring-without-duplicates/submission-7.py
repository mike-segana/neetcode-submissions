class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        maxLen = 0
        for i in range(len(s)):
            while s[i] in charSet:
                charSet.remove(s[l]) #remove every char in s up to and incl repeated char
                l += 1
            charSet.add(s[i])
            maxLen = max(maxLen, i-l + 1)


        return maxLen