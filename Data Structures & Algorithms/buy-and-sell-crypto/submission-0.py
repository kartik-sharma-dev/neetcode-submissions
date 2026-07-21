class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxcount=0

        for i in range(len(prices)):
            l = i+1
            while l < len(prices):

                count = prices[l] - prices[i]
                maxcount= max(maxcount,count)
                l+=1
        return maxcount
                

                
                

                
            
            

            
                


        
                