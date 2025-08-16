def is_pangram(sentence):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    for char in alphabets:
        if not char in sentence.lower():
            return False
    return True
    
    # alphacount = {}
    # for char in sentence.lower():
    #     if char in alphabets:
    #         if char in alphacount.keys():
    #             alphacount[char] += 1
    #         if not char in alphacount.keys():
    #             alphacount[char] = 1
    # if len(alphacount.keys()) < 26:
    #     return False
    # return True
        
