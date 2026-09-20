class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        res=0
        st=set()
        for r in range(len(s)):
            while s[r] in st:
                st.remove(s[left])
                left=left+1
            st.add(s[r])
            res=max(res,r-left+1)
        return res

            
   #