class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #int array piles, where piles[i] is num of bananas in ith pile
        #int h is the number of hours to eat all bananas
        #you may decide bananas per hour rate (k)
        #each hour you may choose a pile and eat k bananas
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