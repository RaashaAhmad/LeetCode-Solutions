class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Brute Force Solution
        '''
        countMap = {}
        for n in nums:
            countMap[n] = 1 + countMap.get(n, 0)
        arrSorted = []
        for num,count in countMap.items():
            arrSorted.append([count, num])
        arrSorted.sort();
        res = []
        while len(res) < k:
            res.append(arrSorted.pop()[1])
        return res
        '''
        #Bucket Sort Solution
        
        freqCounter = [[] for i in range(len(nums) +1)]
        freqMap = {}
        for n in nums:
            freqMap[n] = 1 + freqMap.get(n, 0)
        for num, freq in freqMap.items():
            freqCounter[freq].append(num)
        res = []
        for i in range (len(freqCounter) - 1, -1, -1):
            res.extend(freqCounter[i])
        return res[:k]
        
