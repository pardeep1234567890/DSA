# Implement a document scanning function wordCountEngine,
# which receives a string document and returns a list of all unique words in it and their number of occurrences, 
# sorted by the number of occurrences in a descending order. 
# If two or more words have the same count, they should be sorted according to their order in the original sentence. 
# Assume that all letters are in english alphabet. You function should be case-insensitive, so for instance, 
# the words “Perfect” and “perfect” should be considered the same word.

# The engine should strip out punctuation (even in the middle of a word) and use whitespaces to separate words.

# Analyze the time and space complexities of your solution. Try to optimize for time while keeping a polynomial space complexity.

# Examples:

# input:  document = "Practice makes perfect. you'll only
#                     get Perfect by practice. just practice!"

# output: [ ["practice", "3"], ["perfect", "2"],
#           ["makes", "1"], ["youll", "1"], ["only", "1"], 
#           ["get", "1"], ["by", "1"], ["just", "1"] ]

# My approach 
# firstly i will convert into lowercase and then remove all the punctuations 
# and then using dict count their frequencyies and return the list with frequenices in decending order 
import re 
def wordCountEngine(document):
    new_document = document.lower()
    clean_document = re.sub(r"[^\w\s]","",new_document)
    splited_document = clean_document.split(" ")
    hash_map = {}
    answer = []
    for word in splited_document:
        hash_map[word] = hash_map.get(word,0)+1
    list_hash_map = list(hash_map.items())
    sorted_list= sorted(list_hash_map, key= lambda x : x[1], reverse=True)
    for word , count in sorted_list:
        answer.append([word,str(count)])
    return answer
print(wordCountEngine("Practice makes perfect. you'll only get Perfect by practice. just practice!"))