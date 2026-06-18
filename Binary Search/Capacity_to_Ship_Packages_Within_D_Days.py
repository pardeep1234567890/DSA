# def ship_within_days(weights,days):
#     low = max(weights)
#     high = sum(weight for weight in weights)
#     result = high 
#     while low <= high : # we will not shrink the array we find the exact value so we use low <= high
#         min_cap = (low+high) //2 # we consider this mid as the minimum capicity of ship
#         # we should calculate that that how many days it takes to take over the complete weight 
#         # we can find in such a way that min_cap - weights and the number of times the loop run that will be our number of days to ship the weights 
#         # for i in weights:
#         # day = 0
#         # while min_cap > 0 :
#         #     min_cap = min_cap-weights[day]
#         #     days += 1 
#         # print(day)   
#         # instead of subtract i should do the addition of the weights 
#         current_load = 0
#         day_needed = 1 # we do this because we start to load the packages from day 1 
#         # for weight in weights:
#         #     if current_load < min_cap:
#         #         current_load = current_load+weight
#         #     else : 
#         #         day += 1    
#                 # current_load = 0  ,i was wrong here i have to update this with the current weight 
#         for weight in weights:
#             if current_load +weight>min_cap :
#                 day_needed +=1
#                 current_load = weight 
#             else : 
#                 current_load += weight

#         # now i will write the logic for the min_cap required for the ship to load packages 
#         if day_needed <= days :
#             high = min_cap-1    # here we decrease the capacity 
#             result = min_cap 
#         else:
#             low = min_cap+1    # here we increase the capacity
#     return result        
                

# print(ship_within_days([1,2,3,1,1],4))    

def ship_within_days(weights,days):
    low = max(weights)
    high = sum(weight for weight in weights)
    result = high 
    while low <= high : 
        min_cap = (low+high) //2 
        current_load = 0
        day_needed = 1 
        for weight in weights:
            if current_load +weight>min_cap :
                day_needed +=1
                current_load = weight 
            else : 
                current_load += weight
        if day_needed <= days :
            high = min_cap-1    
            result = min_cap 
        else:
            low = min_cap+1  
    return result        

print(ship_within_days([3,2,2,4,1,4],3))    