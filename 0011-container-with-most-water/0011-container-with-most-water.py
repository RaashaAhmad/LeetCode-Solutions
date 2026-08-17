class Solution:
    def maxArea(self, height: List[int]) -> int:
        #Brute Force Solution
        '''
        maxVol = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                vol = min(height[i], height[j]) * (j - i)
                maxVol = max(maxVol, vol)
        return maxVol
        '''
        l = 0
        r = len(height) - 1
        maxVol = 0
        while l < r:
            vol = min(height[l], height[r]) * (r - l)
            maxVol = max(maxVol, vol)
            if height[l] < height[r]:
                l += 1
            elif height[r] < height[l]:
                r -= 1
            else:
                l += 1
                r -= 1

        return maxVol