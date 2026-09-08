class Solution:
    def countCommas(self, n: int) -> int:
        count = 1
        if n < 1000:
            return 0
        elif n == 1000:
            return 1
        else:
            return count + n -1000