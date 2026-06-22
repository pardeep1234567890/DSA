def daily_temp(temperatures):
    stack = []
    answer = [0] * len(temperatures)
    for i in range(len(temperatures)):
        while stack and temperatures[i]>temperatures[stack[-1]]:
            top_index = stack.pop()
            answer[top_index] = i-top_index # the point is we store the day difference on that day for which we find the warmer temperature
        stack.append(i)
    return answer
print(daily_temp([73,74,75,71,69,72,76,73]))

# for i in range(len(temperatures)):
#         answer.append(0)