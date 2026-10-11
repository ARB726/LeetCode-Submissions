class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        left , right , total , maxFreq = 0 , 0 , 0 , 0
        nums.sort()
        while right < len(nums):
            total += nums[right]

            while nums[right] * (right - left + 1) > total + k: # while window is invalid

               total -= nums[left]
               left +=1

            maxFreq = max(maxFreq , right - left +1)
            right +=1
            
        return maxFreq