class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Brute Force Solution
        '''
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
        '''

        #Hash Set Solution
        '''
        s = set()
        for i in nums:
            if i in s:
                return True
            s.add(i)
        return False
        
        '''

        #Hash Set Length Solution
        return len(set(nums)) < len(nums)