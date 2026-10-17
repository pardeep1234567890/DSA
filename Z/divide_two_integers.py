# 29. Divide Two Integers
# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
# The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.
# Return the quotient after dividing dividend by divisor.
# Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

def divide(dividend, divisor):
    INT_MAX = 2**31 -1
    INT_MIN = -(2**31)
    #  Tackle With Sign
    if dividend < 0 :
        dividend_sign = -1
    else : 
        dividend_sign = 1
    if divisor < 0 :
        divisor_sign = -1
    else:
        divisor_sign = 1
    divd = abs(dividend)
    divr = abs(divisor)

    # Actual Problem start from here 
    total_quetient = 0
    while divr <= divd:
        quetient_count = 1
        divisor_count = divr
        while divisor_count + divisor_count <= divd:
            divisor_count = divisor_count + divisor_count 
            quetient_count = quetient_count + quetient_count 

        divd = divd - divisor_count
        total_quetient += quetient_count
    if dividend_sign != divisor_sign : 
        result =  -total_quetient
    else :
        result = total_quetient
    if result > INT_MAX:
        return INT_MAX
    if result < INT_MIN:
        return INT_MIN
    return result 


print(divide(7,-3))