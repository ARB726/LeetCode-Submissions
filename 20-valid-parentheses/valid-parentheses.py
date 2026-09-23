class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashMap = {'}':'{',']':'[',')':'('}
        
        for i in range(len(s)):
            
            if s[i] == '[' or s[i] =='(' or s[i] =='{':
                stack.append(s[i])
            elif stack and stack[-1] == hashMap[s[i]]:
                stack.pop()
            else:
                return False
        if not stack:
            return True
        else:
            return False