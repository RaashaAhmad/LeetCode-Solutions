class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #Brute Force Solution
        '''
        minSpeed = min(piles)
        while True:
            timeTaken = 0
            for pile in piles:
                timeTaken += math.ceil(pile/ minSpeed)
            if timeTaken < h:
                return minSpeed
            minSpeed += 1
        return minSpeed
        '''
        #Binary Search
        l = 1
        r = max(piles)
        res = r
        while l <= r:
            m = (l + r) // 2
            timeTaken = 0
            for pile in piles:
                timeTaken += math.ceil(float(pile) / m)
            if timeTaken <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res