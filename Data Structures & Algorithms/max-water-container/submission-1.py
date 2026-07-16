class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0 
        right = len(heights)-1
        water =min(heights[left],heights[right])*(right-left)


        while left < right :
            if heights[left]<heights[right]:
                left+=1
                new_water =min(heights[left],heights[right])*(right-left)
                water = max(water,new_water)
            else:
                right-=1
                new_water =min(heights[left],heights[right])*(right-left)
                water = max(water,new_water)
        return water
        