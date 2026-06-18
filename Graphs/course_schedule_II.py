# Steps to solve this problem ,similarly we solve this problem using the kahn's Algo that we used in course schedule Problem 
# 1. So firstly we make the adjacency List 
# 2. then we make a indegree array of length courses 
# 3. then we append the courses(node) in the queue with indegree 0
# 4. then we then pop the node one by by and check it's neighbors , and also after pop the node we pushit into the list to return the order 
# 5. we check the neighbor and reduce it's indegree because it's parent node processed and when the queue will be empty and the loop exit 
# 6. then check the len(order) = numCourses if they equal then loop not exist else exist and return empty list 



# Build the adjacency list
# Build indegree array of length numCourses
# Push all courses with indegree 0 into the queue
# Pop nodes one by one; add each popped node to the order list
# For each neighbor, reduce its indegree by 1 (a prerequisite was completed). If indegree becomes 0, push it to queue
# If len(order) == numCourses → no cycle → return order. Else → cycle exists → return []
# The algorithm is solid — now go implement it! 💪