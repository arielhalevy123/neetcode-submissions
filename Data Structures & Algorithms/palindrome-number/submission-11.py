class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        dup=x
        mult=1
        if x<0:
            return False
        while dup !=0:
            dup=dup//10 
            mult =mult*10
        mult=mult//10
        dev=10
        while mult >= dev // 10:
            if x%dev//(dev//10)!=(x//mult)%10:
                return False
            mult=mult//10
            dev=dev*10
        return True
