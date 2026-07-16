class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        l=0
        r=len(s) -1
       

        while l < r :
                if not s[l].isalnum():
                    l+=1
                    continue
                if not s[r].isalnum():
                    r-=1
                    continue
                if s[l] == " ":
                        l+=1
                        continue
            
                if s[r] == " ":
                        r-=1
                        continue
                if s[l] == s[r]:
                    l+=1
                    r-=1
                else:
                    return False
                    break
        else:
            return True




















        