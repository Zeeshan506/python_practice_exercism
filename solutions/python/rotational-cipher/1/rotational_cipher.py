def rotate(text, key):
    if key < 0:
        raise ValueError("Key can only be positive")
    if isinstance(key,float):
        key = round(key)
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    alpha_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    for char in text:
        if char in alphabets:
            index = ord(char) - ord ('a')
            new_index = (index + key) % 26
            result += chr(new_index + ord('a'))
        if char in alpha_upper:
            index = ord(char) - ord('A')
            new_index = (index + key)%26
            result += chr(new_index + ord('A'))
        if not char in alpha_upper and not char in alphabets:
            result+=char
    return result
    
                    
