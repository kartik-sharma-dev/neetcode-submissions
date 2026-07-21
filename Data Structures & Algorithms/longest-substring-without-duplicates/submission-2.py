class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        stt = set()
        length =0
        for r in range(len(s)):
            while s[r] in stt:
                stt.remove(s[left])
                left+=1
            w = (r-left) +1
            length = max(length,w)
            stt.add(s[r])
        return length
        
            
        