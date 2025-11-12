import re 
def clean_words(words):
    words = words.replace('_', "")
    words = words.replace('.', "")
    words = words.replace("'", "")
    words = re.split('-|\s', words)
    return words

def abbreviate(words):
    cl_words = clean_words(words)
    acr = ""
    for item in cl_words:
        if len(item)>=1:
            acr += item[0].upper()
    return acr
        