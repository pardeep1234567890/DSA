def largest_rectangle(heights):
    stack = []
    max_area = 0
    for i in range(len(heights)):
            if stack and heights[i]>= heights[stack[-1]]:
                  stack.append(i)
            else : 
                  while stack and heights[i]< heights[stack[-1]]:
                    stack_top= stack.pop()
                    if stack :      
                        left_smaller = stack[-1]
                    else :
                        left_smaller= -1  
                    right_smaller = i
                    width = right_smaller-left_smaller-1
                    area = width *heights[stack_top]
                    max_area = max(max_area,area)
                  stack.append(i)  
    # we define this loop because when the loop ends and the inner while loop
    # unable to pop all the elements so we define the same while loop outside 
    # the for loop because to empty the stack                  
    while stack :
         stack_top= stack.pop()
         if stack :      
            left_smaller = stack[-1]
         else :
            left_smaller= -1  
         right_smaller = len(heights)   #Represents an imaginary position "after the last bar"
         width = right_smaller-left_smaller-1
         area = width *heights[stack_top]
         max_area = max(max_area,area)      
    return max_area    

print(largest_rectangle([2,4]))    