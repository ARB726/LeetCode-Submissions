class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack = []
        result = 0

        for op in operations:

            if op == '+':
                
                stack.append(stack[-1] + stack[-2])
                result += stack[-1] and stack[-1]

            elif op == "D":
                stack.append(stack[-1]*2)
                result += stack[-1]
            elif op == "C":
                a =stack.pop()
                result -= a

            else:
                stack.append(int(op))
                result += stack[-1]
        return result