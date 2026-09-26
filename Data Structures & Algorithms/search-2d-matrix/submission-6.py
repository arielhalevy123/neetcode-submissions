class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top=0
        botom=len(matrix)-1
        m=(top+botom)//2
        while top<=botom:
            if matrix[m][0]<=target and matrix[m][-1]>=target:
                l=0
                r=len(matrix[0])-1
                m_row=(l+r)//2
                while l <= r:
                    if matrix[m][m_row]==target:
                        return True
                    if target>matrix[m][m_row]:
                        l=m_row+1
                    else:
                        r=m_row-1
                    m_row=(l+r)//2
            if matrix[m][0]>target:
                botom=m-1
            else:
                top=m+1
            m=(top+botom)//2
        return False


                    

