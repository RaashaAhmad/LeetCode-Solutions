class Solution:
    def findMin(self, nums: List[int]) -> int:
        #Brute Force Solution
        '''min = nums[0]
        for i in nums:
            if i < min:
                min = i
        return min'''
        #Binary Search Solution
        l = 0 
        r = len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]
