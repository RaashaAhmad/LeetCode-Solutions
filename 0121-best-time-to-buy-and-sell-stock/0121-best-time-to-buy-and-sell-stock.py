class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Brute Force Solution
        '''
        maxProf = 0
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                maxProf = max(maxProf, prices[j] - prices[i])
        return maxProf
        '''
        #Sliding Window
        '''
        l = 0
        r = 1
        maxProf = 0
        while r < len(prices):
            if prices[l] >= prices[r]:
                l = r
            else:
                maxProf = max(maxProf, prices[r] - prices[l])
            r += 1
        return maxProf
        '''
        #Dynamic Programming
        maxProf = 0 
        buy = prices[0]
        for sell in prices:
            maxProf = max(maxProf, sell - buy)
            buy = min(buy, sell)
        return maxProf