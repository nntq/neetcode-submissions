class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = {}
        for s in strs:
            k = ''.join(sorted(s))

            if(k not in out):
                out[k] = [s]
            else:
                out[k].append(s)

        return list(out.values())
        