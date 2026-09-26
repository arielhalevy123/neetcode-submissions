class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for st in strs:
           s=s+(str)(len(st))+"#"+st
        return s

    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i<len(s):
           st=""
           stlen=""
           while s[i]!='#':
            stlen=stlen+s[i]
            i+=1
           stlen=(int)(stlen)
           st=s[i+1:i+1+stlen]
           res.append(st)
           i=i+1+stlen
        return res