class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximum = float('-inf')
        left = 0
        right = len(height)-1

        while left < right:

            heights = min(height[left],height[right])
            
            width = right-left
            
            area = heights*width
            print(area)
            maximum = max(area,maximum)
            
            if height[left] < height[right]:
                left +=1
            else:            
                right -=1
                
        return maximum