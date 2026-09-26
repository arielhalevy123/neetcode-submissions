class Solution:
    def isPalindrome(self, s: str) -> bool:
      
        s=s.lower()
        s=s.replace(" ","")
        new_s=""
        for c in s:
            if c.isalnum():
                new_s+=c
        s=new_s
        end=len(s)-1
        new_s=""

        start=0
        while start<end:
            if s[start]!= s[end]:
                return False
            start+=1
            end-=1
        return True
        