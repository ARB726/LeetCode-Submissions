class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        answer = []
        for i in range(len(nums)):

            for j in range(i+1 , len(nums)):
                total = 0
                total += nums[i] + nums[j]

                if total == target:

                    answer.append(i)
                    answer.append(j)

        return answer