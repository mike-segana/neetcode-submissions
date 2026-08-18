class Solution:
    def maxDifference(self, s: str) -> int:
        dictionary = {}
        for char in s:
            dictionary[char] = dictionary.get(char, 0) + 1

        a1 = 0
        a2 = float('inf') #or a2 = 101 because s.length is at most 100

        for value in dictionary.values():
            if value % 2 == 0:
                a2 = min(a2, value)
            else:
                a1 = max(a1, value)

        return a1 - a2