class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        for i in range(len(strs[0])):
            char = strs[0][i] #goes through each char in first string
            for string in strs:
                if i >= len(string) or char != string[i]:
                    return result
            result += char
        
        return result
                