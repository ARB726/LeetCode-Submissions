class Solution:
    def romanToInt(self, s: str) -> int:
        hashMap = {'I': 1 , 'V':5 , 'X':10 , 'L':50 , 'C':100 , 'D':500 , 'M':1000}
        totalSum = 0
        right = len(s) - 1
        for char in range(len(s)-1):
            currentVal = hashMap[s[char]]
            nextVal = hashMap[s[char+1]]

            if currentVal < nextVal:
                totalSum -= currentVal
            else:
                totalSum += currentVal
            
         

        return totalSum + hashMap[s[right]]
