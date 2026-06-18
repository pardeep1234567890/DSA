# Use __init__ to create instance variables so each queue object has its own data. 
# Class-level variables are shared across all instances, which would break the queue implementation.
class MyQueue:
    def __init__(self):
        self.input_stack = []
        self.output_stack = []
    def push(self,val):
        self.input_stack.append(val)

    def pop(self):        
        if not self.output_stack :
            while self.input_stack:
                val = self.input_stack.pop()
                self.output_stack.append(val)
        result = self.output_stack.pop()
        return result
    def peek(self):
        if not self.output_stack:
            while self.input_stack:
                val = self.input_stack.pop()
                self.output_stack.append(val)
        return self.output_stack[-1]
    
    def empty(self):
        return not self.input_stack and not self.output_stack


# written by me 

# class MyQueue:
#     def __init__(self):
#         self.input_stack = []
#         self.output_stack = []
#     def push(self,val):
#         self.input_stack.append(val)

#     def pop(self):        
#         if not self.output_stack :
#             while self.input_stack:
#                 val = self.input_stack.pop()
#                 self.output_stack.append(val)
#         result = self.output_stack.pop()
#         return result
#     def peek(self):
#         # if self.output_stack:
#         #     return self.output_stack [-1]
#         # else : 
#         #     if self.input_stack:
#         #         while self.input_stack:
#         #             val = self.input_stack.pop()
#         #             self.output_stack.append(val)
#         #         return self.output_stack [-1]       
#         #     else:
#         #         return None    
#         if not self.output_stack:
#             while self.input_stack:
#                 val = self.input_stack.pop()
#                 self.output_stack.append(val)
#         return self.output_stack[-1]
