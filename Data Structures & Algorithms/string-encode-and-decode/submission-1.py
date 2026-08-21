class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("$")
            res.append(s)

        return ("".join(res))
        # res = []
        # for s in strs:
        #     res.append(s)
        #     res.append("$")

        # return "".join(res)


    def decode(self, s: str) -> List[str]:
        res = []
        tmp = []
        num = 0
        bfr = []
        reading = False

        for c in s:
            if(num == 0 and not reading):
                if(c == "$"):
                    num = int("".join(tmp))
                    tmp = []
                    if(num == 0):
                        res.append("")
                        num = 0
                    else:
                        reading = True
                else:
                    tmp.append(c)
            else:
                if((num - 1) > 0):
                    bfr.append(c)
                    num -= 1
                else:
                    bfr.append(c)
                    res.append("".join(bfr))
                    num = 0
                    bfr = []
                    reading = False
        
        return res
        # res = []
 
        # bfr = ""
        # for c in s:
        #     if(c != "$"):
        #         bfr += c
        #     else:
        #         res.append(bfr)
        #         bfr = ""

        # return res
