class Solution:

    a = {}
    left = 0

    def encode(self, strs: List[str]) -> str:


        encoded_string = ""

        for i in strs:
            encoded_string +=str(len(i))+"#"+i
        return encoded_string
           
            




# 5#hello5#world
    def decode(self, s: str) -> List[str]:
       
            a = []

            l = 0 
            num = ""
            while l<len(s):
                    if s[l].isdigit():
     
                        num+=s[l]
                        l+=1

                    elif s[l] == "#":
                        lenght = int(num)
                        end = l+1+lenght
                        a.append(s[l+1:end])
                        l = end 
                        num=""

                    
            return a




        

        
























