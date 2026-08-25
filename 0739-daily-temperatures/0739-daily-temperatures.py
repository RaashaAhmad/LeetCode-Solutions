class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #Brute Force Solution
        '''
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            higherTemp = 0
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    higherTemp += 1
                    res[i] = higherTemp
                    break
                higherTemp += 1
        return res
        '''
        #Stack Solution
        res = [0] * len(temperatures)
        stack = []
        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                temp, index = stack.pop()
                res[index] = i - index
            stack.append((t, i))
        return res