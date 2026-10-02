class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            lmap = [0]*26
            for c in s:
                lmap[ord(c)-ord('a')] += 1
            res[tuple(lmap)].append(s)
        return list(res.values())