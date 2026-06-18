def plus_one():
    digits = [1, 2, 3]
    for i in range(len(digits)-1,-1,-1):
        if digits[i] < 9:
            digits[i] = digits[i]+1
            return digits           # use here return statement is very compelsury otherwise it will add 1 into other elements also whcih are less than 9 and we have to just add only in last element 
        else:
            # add 1 into it and transfer the carry to the left side
            # so here i made the mistake because i did not think like coder i was thinking like solving a math problem 
            # so if it is 9 we just set 0 at ones place
            digits[i] = 0
        if i == 0:
            digits.insert(0,1)
    return digits    

print(plus_one())