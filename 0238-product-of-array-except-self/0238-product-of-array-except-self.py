class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Brute Force Solution
        '''
        res = []
        for i in nums:
            product = 1
            for j in nums:
                if i == j:
                    continue
                product *= j
            res.append(product)
        return res
        '''
        #Division Solution
        '''
        if nums.count(0) > 1:
            return [0]*len(nums)
        product = 1
        countZero = 0
        for n in nums:
            if n:
                product *= n
            else:
                countZero +=1

        res= []
        for n in nums:
            if n and countZero:
                res.append(0)
            elif not n and countZero:
                res.append(product)
            else:
                res.append(product//n)
        return res
        '''
        #Prefix and Suffix Solution
        prefix = 1
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        return res