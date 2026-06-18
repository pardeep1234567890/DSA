# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.

def word_break(s,word_dict):
    # i think i should define the hash or array to remember the past words which have checked ?

    def recursive(index):
        if index == len(s):
            return True
        for word in word_dict:
            if s[index:(index+len(word))] in word_dict:
                if recursive(index+len(word)) is True :
                    return True

        return False
    return recursive(0)


