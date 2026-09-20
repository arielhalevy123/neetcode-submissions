class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st=""
        count=0
        max_count=0
        for ch in s:
            if ch not in st:
                st+=ch
                count+=1
                max_count=max(count,max_count)
            else:
                
                st=st[st.index(ch)+1:]+ch
                count=len(st)
        return max_count