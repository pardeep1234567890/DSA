# def Partation_Labels(s):
#     last_occurence = {}
#     j= 0
#     n  = len(s)
#     for i in range(len(s)):
#         last_occurence[s[i]] = i
#     # for j in range(len(s)):
#     while j<n and last_occurence[s[j]] == j:    # 8 != 0 then j =1 , 9!=1 
#         j = j+1


            
    
# print(Partation_Labels("ababcbacadefegdehijhklij"))


# def Partation_Labels(s):
#     last_occurence = {}
#     j= 0
#     n  = len(s)
#     l = []
#     last_index = 0
#     for i in range(len(s)):
#         last_occurence[s[i]] = i
#     # where is the current partation start 
#     # where should your current partitation end 
#     for i in range(len(s)):
#         while j<n and last_occurence[s[i]] == j:    # 8 != 0 then j =1 , 9!=1 
#             j = j+1
#         last_index=j
#         print(last_index)
#         # print(len(s[i:j]))
#         l.append(len(s[i:j]))
#     # return l                
    
# print(Partation_Labels("ababcbacadefegdehijhklij"))

# def Partation_Labels(s):
#     last_occurence = {}
#     j= 0
#     n  = len(s)
#     l = []
#     max_end = 0
#     for i in range(len(s)):
#         last_occurence[s[i]] = i
#     for i in range(len(s)):
#         partation_end = last_occurence[s[i]]    #partation_end = 8,5,8,5,7,5,8,7,8,14,15,11
#         max_end = max(max_end,partation_end)    #max_end = (15,11) = 8,8,8,8,8,8,8,8,8,14,15,15
#         # while max_end > new_max_end
#     new_string = s[max_end]
#     l.append(len(new_string))
#     return l                
    
# print(Partation_Labels("ababcbacadefegdehijhklij"))



# def Partation_Labels(s):
#     last_occurence = {}
#     result = []
#     # s1=""
#     partition_end = 0
#     partition_start = 0
#     for i in range(len(s)):
#         last_occurence[s[i]] = i 
#     for i in range(len(s)):    
#         partition_end = max(partition_end,last_occurence[s[i]])    
#         if i == partition_end:
#             # s1 = s[partition_start:partition_end+1]
#             # partition_start = partition_end+1
#             # result.append(len(s1))
#             result.append(partition_end-partition_start+1)
#             partition_start = i+1
#     return result
    
# print(Partation_Labels("ababcbacadefegdehijhklij"))


def Partation_Labels(s):
    last_occurence = {}
    result = []
    partition_end = 0
    partition_start = 0
    for i in range(len(s)):
        last_occurence[s[i]] = i 
    for i in range(len(s)):    
        partition_end = max(partition_end,last_occurence[s[i]])    
        if i == partition_end:
            result.append(partition_end-partition_start+1)
            partition_start = i+1
    return result
    
print(Partation_Labels("ababcbacadefegdehijhklij"))