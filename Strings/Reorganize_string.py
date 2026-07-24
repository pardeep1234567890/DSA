# 767. Reorganize String
# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

# Return any possible rearrangement of s or return "" if not possible.
import heapq
def reorganie_string(s):

    map = {}
    max_heap = []
    result = ""
    for char in s : 
        map[char] = map.get(char,0)+1
    #how to check that the count is greater or not ?
    # like i can't use loop but i can use max ()
    max_count = max(map.values())
    if (len(s)+1) //2  < max_count :
        return ""
    # i was thinking that i should make max_heap by using hash
    for char,count in map.items() :
        heapq.heappush(max_heap,(-count,char))
    prev_freq,prev_char = 0,None
    while max_heap : 
        neg_count,char = heapq.heappop(max_heap)
        if prev_char != None and prev_freq > 0:
            heapq.heappush(max_heap, (-prev_freq,prev_char))
        count = -neg_count
        result += char
        count -=1 
        prev_freq,prev_char = count,char
    return result

