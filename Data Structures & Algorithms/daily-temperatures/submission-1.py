class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures) #result array initialised with 0s
        stack = [] #will contain [[temp and index],...]
        for index, temp in enumerate(temperatures):
            #while stack not empty and temp > top element in stack
            while stack and temp > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                result[stackIndex] = (index - stackIndex) #hotter day index -  top stack index
            stack.append([temp, index])
        return result