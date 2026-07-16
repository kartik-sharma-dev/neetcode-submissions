class Solution:
    def isPalindrome(self, s: str) -> bool:
        w=0
        l=0


        s = list(s)

        for i in range(len(s)):
            if s[i] != " ":
                    s[w] = s[i]
                    w += 1
        k = "".join(s[:w])
        k=k.lower()
        r=len(k) -1

        while l < r :
                if not k[l].isalnum():
                    l+=1
                    continue
                if not k[r].isalnum():
                    r-=1
                    continue
                if k[l] == k[r]:
                    l+=1
                    r-=1
                else:
                    return False
                    break
        else:
            return True




















        