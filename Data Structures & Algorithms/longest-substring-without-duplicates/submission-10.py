class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        st=set()
        s_max=0
        for r in range(len(s)):
            while s[r] in st:
                st.remove(s[l])
                l+=1
            st.add(s[r])
            s_max=max(s_max,r-l+1)
        return s_max




    
    
    
    
    
    
    
    
    
    
    


            
   #