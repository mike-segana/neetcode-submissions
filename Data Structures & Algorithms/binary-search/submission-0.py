class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            root = left + ((right - left) // 2)
            if nums[root] > target:
                right = root - 1
            elif nums[root] < target:
                left = root + 1
            else:
                return root
        return -1