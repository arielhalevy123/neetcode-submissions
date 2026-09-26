class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par =[i for i in range(n)]
        
        def find(n):
            while n!=par[n]:
                n=par[n]
            return n
        def union(n1,n2):
            par1,par2=find(n1),find(n2)
            if par1==par2:
                return
            par[par2]=par1
            return True
        for n1,n2 in edges:
            union(n1,n2)
        for i in range(n):
            par[i]=find(par[i])

        numset=set(par)
        return len(numset)