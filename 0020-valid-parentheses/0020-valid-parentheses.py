class Solution:
    def isValid(self, s: str) -> bool:
        #Brute Force Solution
        '''
        while s:
            tempLength = len(s)
            s = s.replace('()', '').replace('[]', '').replace('{}', '')
            if tempLength == len(s):
                return False
        return True
        '''
        #Stack Solution
        
        stack = []
        brackets = {'(' : ')', '[':']', '{':'}'}
        for i in s:
            if i in brackets.keys():
                stack.append(i)
            elif i in brackets.values():
                if len(stack) and i == brackets[stack[-1]]:
                    stack.pop()
                else:
                    return False
        return stack == []