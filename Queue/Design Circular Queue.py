# class MyCircularQueue:
#     def __init__(self,k):
#         self.queue = [0]*k
#         self.front = 0   # why we take 0 -> maybe if we insert the element then front can't be -1
#         self.rear = -1
#         self.size = 0
#         self.k = k
#     # here we insert in the queue if insert successful then return True
#     def enQueue(self,val):
#         if self.size != self.k :
#             self.rear = (self.rear+1) % self.k
#             self.queue[self.rear] = val
#             # self.rear +=1
#             self.size += 1
#             return True    
#         else:
#             return False
#     def dequeue(self):
#         if self.size != 0:
#             self.front = (self.front+1) % self.k
#             # self.queue.pop(self.front)
#             # self.front +=1
#             self.size -=1
#             return True
#         else: 
#             return False
#     #  Gets the last item from the queue. If the queue is empty, return -1.
#     def rear(self):
#         if self.size != 0:
#             # val = self.rear.pop()
#             # self.rear -=1  
#             # self.size -=1  
#             return self.queue[self.rear] 
#         else:
#             return -1
#     # int Front() Gets the front item from the queue. If the queue is empty, return -1.
#     def Front(self): 
#         if self.size != 0:
#             # val = self.front.pop()
#             # self.front +=1
#             # self.size -=1
#             return self.queue[self.front]
#         else: 
#             return -1     

#     def isEmpty(self):
#         if self.size ==0:
#             return True
#         else:
#             return False
#     def isFull(self):
#         if self.size == self.k:
#             return True
#         else:
#             return False


class MyCircularQueue:
    def __init__(self,k):
        self.queue = [0]*k
        self.front = 0   
        self.rear = -1
        self.size = 0
        self.k = k
    def enQueue(self,val):
        if self.size == self.k :
            return False
        self.rear = (self.rear+1) % self.k
        self.queue[self.rear] = val
        self.size += 1
        return True    
        
    def dequeue(self):
        if self.size == 0:
            return False
        self.front = (self.front+1) % self.k      # we basically increment the pointers the modulo helps us to wrap the pointers to the fixed size array 
        self.size -=1
        return True
    
    def Rear(self):
        if self.size != 0:
            return self.queue[self.rear] 
        else:
            return -1
    def Front(self): 
        if self.size != 0:
            return self.queue[self.front]
        else: 
            return -1     

    def isEmpty(self):
        if self.size ==0:
            return True
        else:
            return False
        
    def isFull(self):
        if self.size == self.k:
            return True
        else:
            return False