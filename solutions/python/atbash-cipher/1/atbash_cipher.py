ORIGNAL ="abcdefghijklmnopqrstuvwxyz"
CIPHER ="zyxwvutsrqponmlkjihgfedcba"
PUNCTUATIONS = ",.?;:''"


def encode(plain_text):
    plain_text = plain_text.lower()
    new_string = ""
    count = 0
    for char in plain_text:
        if count == 5:
            new_string += " "
            count = 0
        count += 1
        if char == " " or char in PUNCTUATIONS:
            count -= 1
            continue
        if char.isdigit():
            new_string += char
            continue
        pos = ORIGNAL.index(char)
        new_string += CIPHER[pos]
    return new_string.strip()
        


def decode(ciphered_text):
    new_string = ""
    for char in ciphered_text:
        if char == " ":
            continue
        if char.isdigit():
            new_string+=char
            continue
        pos = CIPHER.index(char)
        new_string += ORIGNAL[pos]
    return new_string

