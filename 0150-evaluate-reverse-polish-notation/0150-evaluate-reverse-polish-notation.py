class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #Stack Solution
        numStack = []
        operatorsList = ['+', '-', '*', '/']
        for t in tokens:
            if t not in operatorsList:
                numStack.append(int(t))
            elif t in operatorsList:
                op1 = numStack.pop()
                op2 = numStack.pop()
                if t == '+':
                    numStack.append(op1 + op2)
                elif t == '-':
                    numStack.append(op2 - op1)
                elif t == '*':
                    numStack.append(op1 * op2)
                elif t == '/':
                    numStack.append(int(float(op2) / op1))
        return numStack.pop()