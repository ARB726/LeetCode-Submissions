class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        # hashMap = {']':'[',')':'(','}':'{'}
        hashMap = { '[' : ']' , '{' : '}' , '(' : ')'}

        if len(s) % 2 != 0:
            return False
        for i in range(len(s)):
            
            if s[i] in hashMap:
                stack.append(s[i])

            
            elif stack: 
                if hashMap[stack[-1]] != s[i]:
                    return False
                else:
                    stack.pop()
            else:
                return False
        
        if not stack: return True 
        else: return False                
      

            
