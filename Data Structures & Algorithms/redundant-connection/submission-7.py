class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par =[i for i in range(len(edges)+1)]
        
    
        def find(n):
            
            while n != par[n]:
                n=par[n]
            return n
        def union(n1,n2):
            par1,par2=find(n1),find(n2)
            if par1==par2:
                return False
            
            par[par2]=par1
            
            return True
        for n1,n2 in edges:
            if not union(n1,n2):
                return [n1,n2]
            
        return []
