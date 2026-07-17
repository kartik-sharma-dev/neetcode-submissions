class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a =[]

        t = 0 

        while t<len(nums):
            s = 1
            for i in range(len(nums)):
                if i != t:
                    s = s*nums[i]
            a.append(s)
            t+=1


        return a

        

        