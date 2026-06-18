# Min Stack Problem: Design a stack that supports push, pop, top, and 
# retrieving the minimum element in constant time.

class MinStack:
    """
    This is the CLASS - it's a TEMPLATE/BLUEPRINT
    Think of it like a blueprint for a house - it shows what the house will have,
    but it's not an actual house yet.
    """
    
    def __init__(self):
        """
        __init__ is the CONSTRUCTOR - it runs automatically when you create an object
        This is where you initialize the data for EACH OBJECT
        
        self = reference to THIS specific object
        self.stack = THIS object's stack (each object gets its own!)
        """
        self.stack = []      # Main stack to store all elements
        self.min_stack = []  # Helper stack to track minimum values
        # Each object will have its OWN stack and min_stack
    
    def push(self, val):
        """
        Add an element to the stack
        When you call: obj.push(5)
        - self = obj (the specific object you're using)
        - val = 5 (the value you passed)
        """
        self.stack.append(val)  # Add to THIS object's stack
        
        # Track the minimum: if min_stack is empty or val is new minimum
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    
    def pop(self):
        """
        Remove and return the top element
        """
        if not self.stack:
            return None
        
        val = self.stack.pop()  # Remove from THIS object's stack
        
        # If we're removing the current minimum, remove it from min_stack too
        if val == self.min_stack[-1]:
            self.min_stack.pop()
        
        return val
    
    def top(self):
        """
        Get the top element without removing it
        """
        if not self.stack:
            return None
        return self.stack[-1]
    
    def getMin(self):
        """
        Get the minimum element in constant O(1) time
        """
        if not self.min_stack:
            return None
        return self.min_stack[-1]


# ============ HOW TO USE THE CLASS ============

# CREATE OBJECTS (instances) from the class:
print("=== Creating Objects ===")
stack1 = MinStack()  # Object 1 - has its own stack and min_stack
stack2 = MinStack()  # Object 2 - has its own SEPARATE stack and min_stack

# Each object is independent!
print("\n=== Testing Stack 1 ===")
stack1.push(-2)      # stack1's stack = [-2]
stack1.push(0)       # stack1's stack = [-2, 0]
stack1.push(-3)      # stack1's stack = [-2, 0, -3]
print(f"Stack1 min: {stack1.getMin()}")  # -3
print(f"Stack1 top: {stack1.top()}")      # -3
stack1.pop()         # Remove -3
print(f"Stack1 min after pop: {stack1.getMin()}")  # -2

print("\n=== Testing Stack 2 (independent!) ===")
stack2.push(5)       # stack2's stack = [5]
stack2.push(1)       # stack2's stack = [5, 1]
print(f"Stack2 min: {stack2.getMin()}")  # 1
print(f"Stack2 top: {stack2.top()}")      # 1

# Stack1 and Stack2 are completely separate!
print(f"\nStack1 still has min: {stack1.getMin()}")  # -2 (unchanged)
print(f"Stack2 still has min: {stack2.getMin()}")    # 1 (unchanged)


# ============ KEY TAKEAWAYS ============
"""
1. CLASS = Template
   - MinStack is the blueprint
   
2. OBJECT = Instance created from class
   - stack1 = MinStack() creates an object
   - stack2 = MinStack() creates another separate object
   
3. Each object has its OWN data
   - stack1.stack is different from stack2.stack
   - Changes to stack1 don't affect stack2
   
4. Methods operate on the specific object
   - stack1.push(5) adds 5 to stack1's stack
   - stack2.push(10) adds 10 to stack2's stack (different stack!)
   
5. self = reference to current object
   - When you call stack1.push(5):
     * self = stack1
     * val = 5
     * self.stack.append(val) means "add val to stack1's stack"
"""




class MinStack:
    def __init__(self):
        self.stack = []      
        self.min_stack = []  # Helper stack to track minimum values
        # Each object will have its OWN stack and min_stack
    
    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    
    def pop(self):
        """ Remove and return the top element """
        if not self.stack:
            return None
        
        val = self.stack.pop()  # Remove from THIS object's stack
        
        # If we're removing the current minimum, remove it from min_stack too
        if val == self.min_stack[-1]:
            self.min_stack.pop()
        
        return val
    
    def top(self):
        """
        Get the top element without removing it
        """
        if not self.stack:
            return None
        return self.stack[-1]
    
    def getMin(self):
        """
        Get the minimum element in constant O(1) time
        """
        if not self.min_stack:
            return None
        return self.min_stack[-1]