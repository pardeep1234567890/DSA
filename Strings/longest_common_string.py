def longest_common_prefix(strs):
    new_string =""
    if strs == []:
        return new_string
    if len(strs) == 1:
        new_string += strs[0] 
        return new_string    
    shortest_string = min(strs,key=len)
    # here i did mistake that i should use the range function with shortest_string notwith strs string because the length of longest common string depend on the shortest string
    for i in range(len(shortest_string)):
        for j in range(len(strs)):                
            if shortest_string[i] != strs[j][i]:
                return new_string
        new_string += shortest_string[i] 
    return new_string                  

print(longest_common_prefix(["flower","flow","flight"]))