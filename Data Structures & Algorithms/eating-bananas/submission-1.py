class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        valid = []
        left, right = 1, max(piles)
        while left <= right:
            count = 0
            midpoint = left + ((right - left) // 2)
            for i in range(len(piles)):
                count += math.ceil(piles[i] / midpoint)
            if count <= h:
                valid.append(midpoint)
                right = midpoint - 1
            else:
                left = midpoint + 1
        return min(valid)