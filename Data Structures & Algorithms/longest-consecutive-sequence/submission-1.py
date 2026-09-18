class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set() #sets have O(1) lookup on average, O(n) worst case
        longest_sequence = 0
        for num in nums:
            s.add(num)
        for num in nums:
            if not num - 1 in s:
                count = 1
                current = num
                while current + 1 in s:
                    count += 1
                    current += 1
                longest_sequence = max(count, longest_sequence)
        
        return longest_sequence