class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        zeros = {}
        
        for i in range(len(matrix)):
            row = matrix[i]
            new_row = []
            for j in range(len(row)):
                index_element=j
                element=row[j]
                if element==0:
                    zeros[i] = j
        
        
        for i in range(len(matrix)):
            row = matrix[i]
            new_row = []
            for j in range(len(row)):
                index_element=j
                element=row[j]
                if element==0:
                    if i not in zeros:
                        break
                    
                    # update element in the row
                    for k in range(len(row)):
                        new_row.append(0)

                    matrix[i]=new_row
                    new_row=[]  

                    # update elements in the column
                    for l in range(len(matrix)):
                        row2=matrix[l]

                        for m in range(len(row2)):
                            
                            if m==index_element:
                                matrix[l][m]=0
        return matrix    
