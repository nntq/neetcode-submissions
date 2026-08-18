class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # if(len(s) != len(t)): return False
        
        # tmp = list(s)

        # for c in t:
        #     if c in tmp: tmp.remove(c)

        # return len(tmp) == 0

        if(len(s) != len(t)): return False

        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1

        for char in t:
            if char not in counts or counts[char] == 0:
                return False
            counts[char] -= 1

        return all(v == 0 for v in counts.values())



