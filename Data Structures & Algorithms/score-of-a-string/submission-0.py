class Solution:
    def scoreOfString(self, s: str) -> int:
        counter = 0
        value = ord(s[0])
        for i in range(1, len(s)):
            if value >= ord(s[i]):
                counter += value - ord(s[i])
            else:
                counter += ord(s[i]) - value
            value = ord(s[i])
        return counter