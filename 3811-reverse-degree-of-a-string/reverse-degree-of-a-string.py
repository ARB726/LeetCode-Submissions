class Solution:
    def reverseDegree(self, s: str) -> int:
        totalSum = 0
        for i in range(len(s)):
           totalSum += (123-ord(s[i])) * (i+1)
        return totalSum        