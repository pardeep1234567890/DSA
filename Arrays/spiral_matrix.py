def spiral_matrix():
    matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    res = []
    top,bottom = 0,len(matrix)-1
    left,right = 0,len(matrix[0])-1
    # Here i am setting the boundries
    while left<=right and top <= bottom:
        # traverse from left ->right for top side
        for t in range(left,right+1):
            a =  matrix[top][t]
            res.append(a)
        top += 1 
        # traverse from top ->bottom for right side 
        for r in range(top,bottom+1):
            b = matrix[r][right]
            res.append(b)
        right -=1
        if top <= bottom and left<= right :   #this is the edge case in which if we have only 1 row or 1 column then we can handle using this statement , before update right and left 
            # traverse from right ->left for bottom side
            for b in range(right,left-1,-1):
                c = matrix[bottom][b]
                res.append(c)
            bottom -=1  
            # traverse from bottom ->top for left side
            for l in range(bottom,top-1,-1):
                d =  matrix[l][left]
                res.append(d)
            left +=1
    return res        
print(spiral_matrix())