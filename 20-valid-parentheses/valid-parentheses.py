class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashMap = {'(':')' , '[':']' , '{':'}'}
        

        for char in s:

            if char in hashMap:
                stack.append(char)
            else:
                if not stack or  hashMap[stack[-1]] != char:
                    return False
                else:
                    stack.pop()

            # stack.append(char)

        if stack: 
            return False
        else:
            return True



"""
Example: "(){}["
"""
