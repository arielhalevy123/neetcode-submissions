class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par =[i for i in range(n)]
        components= n
        def find(n):
            while n!=par[n]:
                n=par[n]
            return n
        def union(n1,n2,components):
            par1,par2=find(n1),find(n2)
            if par1==par2:
                return components
            par[par2]=par1
            components=components-1
            return components
        for n1,n2 in edges:
             components=union(n1,n2,components)
        return components