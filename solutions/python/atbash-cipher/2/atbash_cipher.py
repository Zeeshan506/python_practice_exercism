ORIGINAL ="abcdefghijklmnopqrstuvwxyz"
CIPHER ="zyxwvutsrqponmlkjihgfedcba"
PUNCTUATIONS = ",.?;:'' "
def clean_text(text):
    cleaner = str.maketrans(dict.fromkeys(PUNCTUATIONS))
    return text.translate(cleaner)
def add_spaces(text):
    count = 0
    new_string = ""
    for char in text:
        if count == 5:
            new_string += " "
            new_string += char
            count = 1
            continue
        new_string += char
        count +=1
    return new_string
def encode(plain_text):
    trans_table = str.maketrans(ORIGINAL,CIPHER)
    plain_text= plain_text.lower()
    new_string = plain_text.translate(trans_table)
    new_string = clean_text(new_string)
    return add_spaces(new_string).strip()
def decode(ciphered_text):
    trans_table = str.maketrans(CIPHER,ORIGINAL)
    ciphered_text = clean_text(ciphered_text)
    return ciphered_text.translate(trans_table)