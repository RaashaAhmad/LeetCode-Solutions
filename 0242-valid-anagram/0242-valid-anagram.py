class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Brute Force Solution
        '''
        if len(s) != len(t):
            return False
        firstWordList = sorted(s)
        secondWordList = sorted(t)
        for i in range(len(firstWordList)):
            if firstWordList[i] != secondWordList[i]:
                return False
        return True
        '''
        #Hash Map Solution
        '''
        if len(s) != len(t):
        return False
        countS = {}
        countT = {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countS[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
        '''

        #Hash Set Solution
        if (len(s) != len(t)):
            return False
        count = [0]*26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -=1
        for val in count:
            if(val!=0):
                return False
        return True