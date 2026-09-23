class Solution:
    def trap(self, height: list[int]) -> int:
        #Brute Force Soltuion
        '''
        totalWater = 0
        for i in range(len(height)):
            leftHeight = rightHeight = height[i]
            for j in range(i):
                leftHeight = max(leftHeight, height[j])
            for j in range(i + 1, len(height)):
                rightHeight = max(rightHeight, height[j])
            totalWater += min(leftHeight, rightHeight) - height[i]
        return totalWater
        '''
        #Two Pointer Solution
        l = 0
        r = len(height) - 1
        totalWater = 0
        leftHeight = height[l]
        rightHeight = height[r]
        while l < r:
            if leftHeight < rightHeight:
                l += 1
                leftHeight = max(leftHeight, height[l])
                totalWater += leftHeight - height[l]
            else:
                r -= 1
                rightHeight = max(rightHeight, height[r])
                totalWater += rightHeight - height[r]
        return totalWater