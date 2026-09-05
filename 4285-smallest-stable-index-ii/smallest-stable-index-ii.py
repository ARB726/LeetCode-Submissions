class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        result = [0] * len(nums)
        result2 = [0] * len(nums)
        prefix = nums[0]
        for i in range(len(nums)):
            prefix = max(prefix , nums[i])
            result[i] = prefix
        suffix = float('inf')
        for i in range(len(nums)-1 , -1 , -1):
            suffix = min(nums[i],suffix)
            result2[i] = suffix
        
        for i in range(len(nums)):
            total = result[i] - result2[i]
            if total <=k:
                return i

        return -1



