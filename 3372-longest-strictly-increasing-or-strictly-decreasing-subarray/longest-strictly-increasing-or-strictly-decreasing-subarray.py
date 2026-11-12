class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        Ascend = 1
        Descend = 1
        maxLength = 1

        for i in range(len(nums)-1):

            if nums[i+1] > nums[i]:
                Ascend += 1
                Descend = 1

            elif nums[i+1] < nums[i]:
                Ascend =1
                Descend +=1

            else:
                Ascend = 1
                Descend = 1

            maxLength = max(Ascend,Descend,maxLength)

        return maxLength