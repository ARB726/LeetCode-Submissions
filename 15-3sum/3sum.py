class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: continue
            j = i + 1
            k = len(nums)-1

            while j < k:

                totalSum = nums[i] + nums[j] + nums[k]    

                if totalSum > 0:
                    k -=1
                
                elif totalSum < 0:
                    j +=1

                else:
                    result.append([nums[i],nums[j],nums[k]])

                    while j < k and nums[j] == nums[j+1]:
                        j +=1
                    
                    while j < k and nums[k] == nums[k-1]:
                        k -=1
                    
                    j+=1
                    k-=1

        return result



    

"""
- create a empty list
- sort array
- use a for loop to iterate until next one is not same and index is greater than 0
    - create a second pointer and third pointer
    - use a while loop to check until 2nd and 3rd pointers don't meet
    - if sum is greater than 0 decrease last pointer
    - if sum is less than then increase second pointer
    - else create a list and add to the original list
    - after that shift second and third pointer as well

"""