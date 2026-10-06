class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        minLength = float('inf')
        if len(needle) > len(haystack):
            return -1
        for char in range(len(haystack)-len(needle)+1):
            if haystack[char:char + len(needle) ] == needle:
                return char
        return -1