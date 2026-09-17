class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        maxheight = float('-inf')
        
        while left < right:

            length = right - left 

            width = min(height[left],height[right])

            area = length * width

            maxheight = max(area , maxheight)

            if height[left] < height[right]:

                left +=1
            
            else:
                right -=1

        return maxheight
