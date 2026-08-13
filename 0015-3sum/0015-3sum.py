class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        #Brute Force Solution
        '''
        res = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp = [nums[i], nums[j], nums[k]]
                        res.add(tuple(temp))
        return [list(i) for i in res]
        '''

        #Binary Search
        '''
        res = set()
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            seen = set()
            for j in range(i + 1, len(nums)):
                complement = -(nums[i] + nums[j])
                if complement in seen:
                    res.add((nums[i], complement, nums[j]))
                seen.add(nums[j])
        return [list(i) for i in res]
        '''

        #Two Pointer
        res = set()
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l<r:
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    temp = [nums[i], nums[l], nums[r]]
                    res.add(tuple(temp))
                    l += 1
                    r -= 1
        return [list(i) for i in res]