class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = []
        for i in range(len(arr)-1):
            if i != len(arr):
                print(max(arr[i+1:]))
                result.append(max(arr[i+1:]))
        result.append(-1)
        return result