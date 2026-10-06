class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        left , right , result = 0 , n ,[]

        while left <= n and right < len(nums):

            result.append(nums[left])
            result.append(nums[right])
            left +=1
            right +=1

        return result