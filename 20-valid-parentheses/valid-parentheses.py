class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        hashMap = {
            '[':']' ,
            '{':'}' ,
            '(':')'
        }


        for char in s:

            if char in hashMap:
                stack.append(char)
            
            elif stack and hashMap[stack[-1]] == char: # this line basically means is that current char will always be closing bracket in this and we check if the top is opening bracket then we can pop it because in the previous if statement we check if char is key in hashMap(means opening brackets)
                stack.pop()
            else:
                return False
                break

        return not stack