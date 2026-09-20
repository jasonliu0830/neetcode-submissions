class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) == len(t):
            smap,tmap={},{}
            for i in range(len(s)):
                smap[s[i]] = 1 + smap.get(s[i],0)
                tmap[t[i]] = 1 + tmap.get(t[i],0)
            for j in smap:
                if smap[j]!=tmap.get(j,0):
                    return False
            return True
        else:
            return False
