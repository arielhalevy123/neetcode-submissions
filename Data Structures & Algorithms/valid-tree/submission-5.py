class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        par=[i for i in range(n)]
        size=[1]*n
        components=n
        def find(n):
            while n!=par[n]:
                par[n]=par[par[n]]
                n=par[n]
            return n
        def union(n1,n2):
            par1,par2=find(n1),find(n2)
            if par1==par2:
                return False
            if size[par1]>size[par2]:
                par[par2]=par1
                size[par1]+=size[par2]
            else:
                par[par1]=par2
                size[par2]+=size[par1]
            return True
        
        for n1,n2 in edges:
            if not union(n1,n2):
                return False
            components=components-1

        if components==1:
            return True
        return False