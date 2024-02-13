matrix1 = [[1,2,-1],[4,-1,6],[7,8,9]]
matrix2 = [[-1,0,0,2,2],[2,0,0,2,1],[4,3,2,1,1],[-1,-1,0,2,4],[1,0,3,-1,0]]
from math import inf
def modify_matrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    for c in range(cols):
        change_idx = [-1] * rows
        max_val = -inf
        for r in range(rows):
            if matrix[r][c] == -1:
                change_idx[r] = r 
            max_val = max(max_val, matrix[r][c])
        
        for i in range(len(change_idx)):
            if change_idx[i] != -1:
                matrix[i][c] = max_val

modify_matrix(matrix1)
modify_matrix(matrix2)

print(matrix1)
#  [[1,2,9],[4,8,6],[7,8,9]]
print(matrix2)
# [[4,0,0,2,2],[2,0,0,2,1],[4,3,2,1,1],[4,3,0,2,4],[1,0,3,2,0]]