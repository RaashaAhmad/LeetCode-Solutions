class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Brute Force Solution
        '''
        if not len(nums):
            return 0
        res = 0
        uniqueNums = set(nums)
        for n in uniqueNums:
            count = 0
            curr = n
            while curr in nums:
                count +=1
                curr +=1
            res = max(res, count)
        return res
        '''
        #Checking Previous Solution
        '''
        if not len(nums):
            return 0
        res = 0
        uniqueNums = set(nums)
        for n in uniqueNums:
            if n-1 not in uniqueNums:
                count = 1
                while n+count in uniqueNums:
                    count += 1
                res = max(count,res)
        return res
        '''
        #Hash Map Solution
        if not len(nums):
            return 0
        res = 0
        uniqueNums = set(nums)
        mapLength = defaultdict(int)
        res = 0
        for n in uniqueNums:
            if not mapLength[n]:
                mapLength[n] = mapLength[n-1] + mapLength[n+1] + 1
                mapLength[n - mapLength[n - 1]] = mapLength[n]
                mapLength[n + mapLength[n + 1]] = mapLength[n]
                res  = max(res, mapLength[n])
        return res