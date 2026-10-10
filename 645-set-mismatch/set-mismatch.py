class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        hashSet = set()
        result = []
        maxNum = 0
        for i in range(len(nums)):

            if nums[i] in hashSet:
                additional = nums[i]

            hashSet.add(nums[i])

        for i in range(1,len(nums)+1):

            if i not in hashSet:
                missing = i

        return [additional , missing] 
               
      