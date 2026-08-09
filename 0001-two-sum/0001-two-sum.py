class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Brute Force Solution
        '''
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []
        '''

        #Hash Map Solution
        '''
        numsMap = {}
        for i,n in enumerate(nums):
            numsMap[n] = i
        for i,n in enumerate(nums):
            if target - n in numsMap and numsMap[target - n] != i:
                return [i, numsMap[target - n]]
        return []
        '''
        #Single Parse Solution
        parsedMap = {}
        for i,n in enumerate(nums):
            d = target - nums[i]
            if d in parsedMap:
                return [parsedMap[d],i]
            parsedMap[n] = i
        return []