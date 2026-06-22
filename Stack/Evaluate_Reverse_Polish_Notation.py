def reverse_polish_notation(tokens):
    stack =[]
    for val in tokens:
        if val not in ["+", "-", "/", "*"]:
            int_val= int(val)
            stack.append(int_val)
        else:
            operator = val
            operand2= stack.pop()
            operand1= stack.pop()
            if operator == "+" :   
                result = operand1 + operand2  
                stack.append(result)
            elif operator == "-" :   
                result = operand1 - operand2  
                stack.append(result)
            elif operator == "/" :   
                result = int(operand1 / operand2)  
                stack.append(result)        
            elif operator == "*" :   
                result = operand1 * operand2  
                stack.append(result)
    return stack[-1]

print(reverse_polish_notation(tokens =
["4","-2","/","2","-3","-","-"]))    

# Simple Analogy
# if it is not an operator then append in the stack after changing into the integer 
# otherwise we pop the top two operand and perform operation on them and append the result in to the stack 
# and at last return the top element