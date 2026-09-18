class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        st_open="({["
        st_close=")}]"
        for ch in s:
            if ch in st_open:
                stack.append(ch)

            if ch in st_close and not stack:
                return False
            if ch in st_close and stack and stack[-1] in st_open:

                if ch == "]" and stack[-1]=="[":
                    stack.pop() 
                elif ch == ")" and stack[-1]=="(":
                    stack.pop() 
                elif ch == "}" and stack[-1]=="{":
                    stack.pop()
                else:
                    return False
            
            
        if not stack:
            return True
        return False
            
            
            
        