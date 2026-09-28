class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for char in s:
            if char == ')':
                result = ""
                while stack[-1] != '(':
                    a = stack.pop()
                    result += a
                stack.pop()
                for char in result:
                    stack.append(char)
            else:
                stack.append(char)
        
        return "".join(stack)