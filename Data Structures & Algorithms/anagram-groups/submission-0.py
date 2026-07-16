class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a={}
        for i in strs:
                key = "".join(sorted(i))

                if key in a:
                    a[key].append(i)
                else:
                    a[key] = [i]
        return (list(a.values()))



           
         


        