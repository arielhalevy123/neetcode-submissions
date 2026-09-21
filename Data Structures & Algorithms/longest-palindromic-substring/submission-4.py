class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest=""
        for center in range(len(s)):
            l=1
            r=1
            corrent=""+s[center]
            while center-l>=0 and center+r<len(s) and s[center-l]==s[center+r]:
                corrent=s[center-l]+corrent+s[center+r]
                l=l+1
                r=r+1

            l_e=0
            r_e=1
            corrent_e=""
            while center-l_e>=0 and center+r_e<len(s) and s[center-l_e]==s[center+r_e]:
                corrent_e=s[center-l_e]+corrent_e+s[center+r_e]
                l_e=l_e+1
                r_e=r_e+1
            if len(corrent)>len(longest):
                longest=corrent
            if len(corrent_e)>len(longest):
                longest=corrent_e
        return longest
            



        