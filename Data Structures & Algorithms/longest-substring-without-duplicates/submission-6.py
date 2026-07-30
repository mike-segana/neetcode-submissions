class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = list(s)
        maxLen = 0
        if len(chars) == 0:
            return 0
        if len(chars) == 1:
            return 1
        for i in range(len(chars)):
            substring = []
            substring.append(chars[i])
            for j in range(i+1, len(chars)):
                if not chars[j] in substring:
                    substring.append(chars[j])
                else:
                    maxLen = max(maxLen, len(substring))
                    substring = []
                maxLen = max(maxLen, len(substring))
            
        return maxLen