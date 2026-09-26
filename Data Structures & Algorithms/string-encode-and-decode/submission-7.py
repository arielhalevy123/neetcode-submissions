class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for st in strs:
            s=s+st+"#*#"
        return s

    def decode(self, s: str) -> List[str]:
        res=[]
        st=""
        i=0
        while i<len(s):

            if i + 2 < len(s) and s[i]=="#" and s[i+1]=="*"and s[i+2]=="#":
                i=i+3
                res.append(st)
                st=""
                continue
            if i < len(s):
                st=st+s[i]
                i=i+1

            
            
        return res

            
