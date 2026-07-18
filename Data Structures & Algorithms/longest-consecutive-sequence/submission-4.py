class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
               return 0
        nums.sort()
        left=0
        right = left+1
        max_streak =  0
        current_streak=0
        while right<len(nums):
            
               
            
            if nums[left]+1==nums[right]:
                left+=1
                right+=1
                current_streak+=1
                max_streak = max(max_streak,current_streak)
            elif nums[left]==nums[right]:
                left+=1
                right+=1
                
            else:
                left+=1
                right+=1
                current_streak = 0
                
                
        return max_streak + 1