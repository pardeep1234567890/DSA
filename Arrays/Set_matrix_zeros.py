# In python a matrix is defined using a list of lists 
# len(matrix[0]) ,Length of first row = number of columns

# this is the three step solution 
# first we set the poistions of 0 in row in rowSet and column in colSet 
# then we check if either one position is in the either set we set that poitioned element to zero
# def matrix_zeros():
#     matrix = [
#         [1, 1, 1],
#         [1, 0, 1],
#         [1, 1, 1]
#     ]
#     row_set = set()
#     col_set = set()
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             if matrix[i][j] == 0:
#                 row_set.add(i)
#                 col_set.add(j)
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             if i in row_set or j in col_set:
#                 matrix[i][j] = 0    # if either one position is in the either set we set that poitioned element to zero 
#     return matrix                      

# print(matrix_zeros())



# we're using the first row/column as markers instead of extra sets.
# def matrix_zeros():
#     matrix = [
#         [1, 1, 1],
#         [1, 0, 1],
#         [1, 1, 1]
#     ]
#     col0 = 1
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             if matrix[i][j] == 0:
#                 matrix[i][0] = 0
#                 if j !=0:
#                     matrix[0][j] = 0
#                 if j == 0:
#                     col0 = 0
#     for i in range(1,len(matrix)):
#         for j in range(1,len(matrix[0])):
#             if matrix[i][0] ==0 or matrix[0][j] ==0 :
#                 matrix[i][j] =0  
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             if matrix[0][0] == 0:
#                 matrix[0][j] = 0 #this is row 
#             if col0 == 0 :
#                 matrix[i][0]  = 0

#     return matrix                      

# print(matrix_zeros())


def matrix_zeros():
    matrix = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    col0 = 1
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                if j !=0:
                    matrix[0][j] = 0
                if j == 0:
                    col0 = 0
    for i in range(1,len(matrix)):
        for j in range(1,len(matrix[0])):
            if matrix[i][0] ==0 or matrix[0][j] ==0 :
                matrix[i][j] =0  
    if matrix[0][0] == 0:
        for j in range(len(matrix[0])):
            matrix[0][j] =0 
    if col0 == 0:    
        for i in range(len(matrix)):
            matrix[i][0] =0

    return matrix                      

print(matrix_zeros())