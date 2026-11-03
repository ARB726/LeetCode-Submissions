class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxNum = max(nums)
        count = 0

        for num in nums:

            count += maxNum - num
        
        return count